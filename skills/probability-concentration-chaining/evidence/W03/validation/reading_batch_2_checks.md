# W03 second-batch mechanical checks — 2026-11-14

These checks validate file identity/page coverage and skill metadata structure. They do not replace reading the papers or prove the cited mathematical results.

## PDF identity and page counts

SHA-256 values for all six records marked `fulltext_read` in `evidence/W03/sources.json` match the bytes at their recorded local paths. PDFKit successfully parsed these physical page counts:

| Local ID | PDF pages |
|---|---:|
| P001 | 32 |
| P002 | 27 |
| P003 | 15 |
| P004 | 63 |
| P012 | 34 |
| P018 | 53 |

For each of the six records, `read_pages` is exactly the sequence `1..pdf_page_count`, and `review_status` remains `pending`.

## Manifest counts

Python standard-library JSON checks passed: 34 source records, 6 documented full-text reads, 26 acquired but unread PDFs, and 2 entries without local PDFs. All counts match `evidence/W03/status.json`.

## Skill metadata

Ruby's standard YAML parser validated the skill frontmatter as a mapping with allowed keys, valid hyphen-case name, and a description within the configured length limit. The provided `quick_validate.py` could not run because this Python environment lacks the `yaml` module; the Ruby check covered its frontmatter rules.

## Mathematical sanity computation

`P012_gaussian_max_check.py` computes finite iid standard-Gaussian maxima numerically for `n=1,10,100` and `epsilon=.01,.1`. All six displayed instances satisfy the numerical comparison with Theorem 2.1's stated right-hand side. This is a finite numerical sanity check only, not a proof of the theorem.
