#!/usr/bin/env python3
"""Small scholarly CLI. API metadata and valid PDFs still require identity review."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit, unquote
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

LAST_REQUEST = 0.0
UA = "LiteratureSearchDownload/1.0 (academic metadata and public fulltext)"


def now():
    return datetime.now(timezone.utc).isoformat()


def request(url):
    global LAST_REQUEST
    if urlsplit(url).scheme not in ("http", "https"):
        raise ValueError("only HTTP(S) URLs are supported")
    time.sleep(max(0, 3 - (time.monotonic() - LAST_REQUEST)))
    LAST_REQUEST = time.monotonic()
    return urlopen(Request(url, headers={"User-Agent": UA}), timeout=30)


def safe_error(exc):
    # Do not expose URLs, contact emails, tokens or request bodies.
    if isinstance(exc, HTTPError):
        result = {"kind": "http_error", "http_status": exc.code}
        retry = exc.headers.get("Retry-After")
        if retry:
            result["retry_after"] = retry[:100]
        return result
    if isinstance(exc, URLError):
        return {"kind": "network_error", "detail": type(exc.reason).__name__}
    known_messages = {
        "not a PDF header", "encrypted PDF requires separate review",
        "encrypted or repaired PDF requires separate review", "empty PDF",
        "transfer budget exceeded", "incomplete transfer", "credential-bearing URL rejected",
        "existing file has no matching resume record", "invalid DOI",
        "PDF parser missing: use Python with PyMuPDF or pypdf",
        "arXiv API returned an error entry", "output exists; choose a new output path",
        "choose a new report path distinct from inputs/PDFs", "duplicate manifest id",
        "papers must be a list of objects",
        "use safe unique ids such as 001; DOI/arXiv IDs containing slashes must be renamed",
        "only HTTP(S) URLs are supported",
    }
    if str(exc) in known_messages:
        return {"kind": type(exc).__name__, "detail": str(exc)}
    return {"kind": type(exc).__name__}


def get_json(url):
    with request(url) as response:
        return json.load(response)


def write_json(path, data):
    path = Path(path)
    if path.exists():
        raise FileExistsError("output exists; choose a new output path")
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects prior artifacts.
    with path.open("x", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def doi_value(value):
    value = unquote(value.strip())
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)", "", value, flags=re.I)
    if not re.fullmatch(r"10\.\d{4,9}/\S+", value, flags=re.I):
        raise ValueError("invalid DOI")
    return value.lower()


def first(items):
    return items[0] if items else None


def crossref_record(item):
    date = item.get("published", {}).get("date-parts", [])
    return {
        "id": item.get("DOI"), "doi": item.get("DOI"),
        "title": first(item.get("title", [])),
        "authors": [", ".join(x for x in (a.get("family"), a.get("given")) if x)
                    or a.get("name", "") for a in item.get("author", [])],
        "year": date[0][0] if date and date[0] else None,
        "venue": first(item.get("container-title", [])),
        "type": item.get("type"), "volume": item.get("volume"),
        "issue": item.get("issue"), "pages": item.get("page"),
        "metadata_sources": ["https://api.crossref.org/works/" + quote(item.get("DOI", ""), safe="")],
        "landing_url": item.get("URL"), "verification_status": "pending_verification",
        "reading_scope": "metadata", "version": "unknown",
        "link_hints": [{"url": v.get("URL"), "content_type": v.get("content-type"),
                        "source": "crossref_link", "version": v.get("content-version", "unknown")}
                       for v in item.get("link", [])],
        "pdf_candidates": [],
    }


def search(args):
    result = {"query": args.query, "source": args.source, "retrieved_at": now(),
              "papers": [], "errors": []}
    try:
        if args.source == "crossref":
            params = {"query.bibliographic": args.query, "rows": args.limit}
            data = get_json("https://api.crossref.org/works?" + urlencode(params))
            result["papers"] = [crossref_record(v) for v in data["message"]["items"]]
        else:
            url = "https://export.arxiv.org/api/query?" + urlencode({
                "search_query": args.query, "start": 0, "max_results": args.limit,
                "sortBy": "relevance", "sortOrder": "descending"})
            with request(url) as response:
                root = ET.fromstring(response.read(10 * 1024 * 1024))
            ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
            for entry in root.findall("a:entry", ns):
                identifier = entry.findtext("a:id", "", ns).split("/abs/")[-1]
                if identifier.endswith("/errors") or identifier == "http://arxiv.org/api/errors":
                    raise ValueError("arXiv API returned an error entry")
                links = [v.attrib for v in entry.findall("a:link", ns)]
                pdfs = [{"url": v["href"], "source": "arxiv", "version": identifier}
                        for v in links if v.get("title") == "pdf"]
                result["papers"].append({
                    "id": identifier, "arxiv_id": identifier,
                    "doi": entry.findtext("x:doi", None, ns),
                    "title": " ".join(entry.findtext("a:title", "", ns).split()),
                    "authors": [v.findtext("a:name", "", ns) for v in entry.findall("a:author", ns)],
                    "year": int(entry.findtext("a:published", "", ns)[:4]),
                    "published": entry.findtext("a:published", None, ns),
                    "updated": entry.findtext("a:updated", None, ns),
                    "venue": "arXiv", "version": "preprint:" + identifier,
                    "journal_reference_hint": entry.findtext("x:journal_ref", None, ns),
                    "abstract": " ".join(entry.findtext("a:summary", "", ns).split()),
                    "metadata_sources": ["https://arxiv.org/abs/" + identifier],
                    "verification_status": "pending_verification", "reading_scope": "metadata",
                    "pdf_candidates": [], "link_hints": pdfs})
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, ET.ParseError, OSError) as exc:
        result["errors"].append({"source": args.source, **safe_error(exc)})
    write_json(args.output, result)
    return 1 if result["errors"] else 0


def resolve(args):
    doi = doi_value(args.doi)
    result = {"doi": doi, "retrieved_at": now(), "papers": [], "errors": [], "notes": []}
    try:
        result["papers"] = [crossref_record(get_json(
            "https://api.crossref.org/works/" + quote(doi, safe=""))["message"])]
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, OSError) as exc:
        result["errors"].append({"source": "crossref", **safe_error(exc)})
    email = os.environ.get("LITERATURE_EMAIL")
    if not email:
        result["notes"].append("Unpaywall skipped: no user-provided LITERATURE_EMAIL")
    else:
        try:
            data = get_json("https://api.unpaywall.org/v2/" + quote(doi, safe="") + "?" + urlencode({"email": email}))
            result["oa"] = {"is_oa": data.get("is_oa"), "oa_status": data.get("oa_status"),
                            "locations": [{k: loc.get(k) for k in (
                                "url_for_pdf", "url_for_landing_page", "version", "license", "host_type")}
                                for loc in data.get("oa_locations", [])]}
        except (HTTPError, URLError, TimeoutError, ValueError, KeyError, OSError) as exc:
            result["errors"].append({"source": "unpaywall", **safe_error(exc)})
    write_json(args.output, result)
    return 1 if result["errors"] else 0


def pdf_info(path):
    with Path(path).open("rb") as handle:
        if not handle.read(1024).lstrip().startswith(b"%PDF-"):
            raise ValueError("not a PDF header")
    try:
        import fitz
    except ImportError:
        from pypdf import PdfReader
        reader = PdfReader(str(path), strict=True)
        if reader.is_encrypted:
            raise ValueError("encrypted PDF requires separate review")
        pages = len(reader.pages)
        text = reader.pages[0].extract_text() if pages else ""
    else:
        with fitz.open(path) as document:
            if document.needs_pass or document.is_repaired:
                raise ValueError("encrypted or repaired PDF requires separate review")
            pages = document.page_count
            # Access each page to catch broken page trees; identity remains separate.
            for index in range(pages):
                document.load_page(index)
            text = document[0].get_text() if pages else ""
    if pages < 1:
        raise ValueError("empty PDF")
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return {"pages": pages, "sha256": digest.hexdigest(), "bytes": Path(path).stat().st_size,
            "first_page_preview": (text or "")[:1500]}


def download(args):
    try:
        import fitz
    except ImportError:
        try:
            import pypdf
        except ImportError:
            raise RuntimeError("PDF parser missing: use Python with PyMuPDF or pypdf")
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    papers = manifest if isinstance(manifest, list) else manifest["papers"]
    if not isinstance(papers, list) or not all(isinstance(p, dict) for p in papers):
        raise ValueError("papers must be a list of objects")
    output = Path(args.out).resolve()
    ids = []
    for paper in papers:
        identifier = str(paper["id"])
        if not re.fullmatch(r"[\w.-]{1,120}", identifier) or identifier in (".", ".."):
            raise ValueError("use safe unique ids such as 001; DOI/arXiv IDs containing slashes must be renamed")
        if identifier in ids:
            raise ValueError("duplicate manifest id")
        ids.append(identifier)
    if Path(args.report).exists() or Path(args.report).resolve() in (
            Path(args.manifest).resolve(), *(output / (i + ".pdf") for i in ids)):
        raise FileExistsError("choose a new report path distinct from inputs/PDFs")
    previous = {}
    if args.resume:
        previous = {str(v["id"]): v for v in json.loads(Path(args.resume).read_text(encoding="utf-8"))["papers"]}
    output.mkdir(parents=True, exist_ok=True)
    report = {"retrieved_at": now(), "papers": []}
    for paper, identifier in zip(papers, ids):
        row = {"id": identifier, "title": paper.get("title"), "status": "not_obtained",
               "identity_status": "pending", "attempts": []}
        report["papers"].append(row)
        dest = output / (identifier + ".pdf")
        candidates = paper.get("pdf_candidates", [])[:5]
        if dest.exists():
            try:
                info = pdf_info(dest)
                old = previous.get(identifier, {})
                if old.get("sha256") != info["sha256"] or old.get("url") not in [v.get("url") for v in candidates]:
                    raise FileExistsError("existing file has no matching resume record")
                row.update(info, status="downloaded_pending_identity", path=str(dest),
                           url=old["url"], source=old.get("source"), version=old.get("version"), reused=True)
            except Exception as exc:
                row.update(status="existing_file_conflict", error=safe_error(exc))
            continue
        for candidate in candidates:
            url = candidate.get("url", "")
            attempt = {"url": url, "source": candidate.get("source")}
            row["attempts"].append(attempt)
            temp = None
            try:
                # Do not accept URLs with embedded credentials.
                parsed = urlsplit(url)
                if parsed.username or parsed.password or any(k in parsed.query.lower() for k in ("api_key=", "token=", "email=")):
                    attempt["url"] = "[credential-bearing URL rejected]"
                    raise ValueError("credential-bearing URL rejected")
                with request(url) as response, tempfile.NamedTemporaryFile(dir=output, suffix=".part", delete=False) as handle:
                    temp = Path(handle.name)
                    start = time.monotonic()
                    size = 0
                    while chunk := response.read(64 * 1024):
                        size += len(chunk)
                        if size > args.max_mib * 1024 * 1024 or time.monotonic() - start > 120:
                            raise ValueError("transfer budget exceeded")
                        handle.write(chunk)
                    if response.headers.get("Content-Length") and size != int(response.headers["Content-Length"]):
                        raise ValueError("incomplete transfer")
                info = pdf_info(temp)
                # Hard link is an atomic no-overwrite commit on the same filesystem.
                os.link(temp, dest)
                row.update(info, status="downloaded_pending_identity", path=str(dest),
                           url=url, source=candidate.get("source"), version=candidate.get("version", "unknown"))
                attempt["status"] = "structure_valid"
                break
            except Exception as exc:
                attempt.update(status="failed", error=safe_error(exc))
                if isinstance(exc, HTTPError) and exc.code == 429:
                    row["status"] = "rate_limited"
                    break
            finally:
                if temp is not None:
                    temp.unlink(missing_ok=True)
        if not candidates:
            row["reason"] = "no reviewed public PDF candidates"
    write_json(args.report, report)
    return 1 if any(v["status"] != "downloaded_pending_identity" for v in report["papers"]) else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("search")
    p.add_argument("--source", choices=["crossref", "arxiv"], required=True)
    p.add_argument("--query", required=True)
    p.add_argument("--limit", type=int, default=15)
    p.add_argument("--output", required=True)
    p.set_defaults(run=search)
    p = sub.add_parser("resolve")
    p.add_argument("--doi", required=True)
    p.add_argument("--output", required=True)
    p.set_defaults(run=resolve)
    p = sub.add_parser("download")
    p.add_argument("--manifest", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--resume")
    p.add_argument("--max-mib", type=int, default=100)
    p.set_defaults(run=download)
    args = parser.parse_args()
    if getattr(args, "limit", 1) not in range(1, 101) or getattr(args, "max_mib", 1) < 1:
        parser.error("limit must be 1..100 and max-mib must be positive")
    if getattr(args, "output", None) and Path(args.output).exists():
        parser.error("output exists; choose a new output path")
    try:
        return args.run(args)
    except Exception as exc:
        print(json.dumps({"error": safe_error(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
