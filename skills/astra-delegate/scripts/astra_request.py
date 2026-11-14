#!/usr/bin/env python3
"""Request a bounded Astra text consultation. Reads the prompt from stdin."""
import argparse
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request


def extract(response):
    return "\n".join(item.get("text", "") for out in response.get("output", [])
                     if out.get("type") == "message" for item in out.get("content", [])
                     if item.get("type") == "output_text")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"], default="high")
    parser.add_argument("--max-output-tokens", type=int, default=4096)
    args = parser.parse_args()
    if not 1 <= args.max_output_tokens <= 128000:
        parser.error("--max-output-tokens must be between 1 and 128000")
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        skill = (Path(__file__).resolve().parent.parent / "SKILL.md").read_text()
        key = next((line.split("=", 1)[1].strip() for line in skill.splitlines()
                    if line.startswith("OPENAI_API_KEY_SAVED=")), None)
    if not key:
        print("OPENAI_API_KEY is not set in this process; provide a new key securely.", file=sys.stderr)
        return 2
    prompt = sys.stdin.read()
    if not prompt.strip():
        print("No task provided on stdin.", file=sys.stderr)
        return 2
    body = json.dumps({"model": "gpt-6-astra", "input": prompt,
                       "reasoning": {"effort": args.effort},
                       "max_output_tokens": args.max_output_tokens,
                       "store": False}).encode("utf-8")
    request = urllib.request.Request("https://api.openai.com/v1/responses", data=body,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        print(f"OpenAI API request failed (HTTP {exc.code}); check access, billing, and limits.", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        print(f"OpenAI API request failed ({type(exc).__name__}); no automatic retry.", file=sys.stderr)
        return 1
    status = data.get("status", "unknown")
    print(json.dumps({"model": data.get("model"), "status": status,
                      "text": extract(data), "usage": data.get("usage"),
                      "incomplete_details": data.get("incomplete_details")}, ensure_ascii=False))
    return 0 if status == "completed" else 1


if __name__ == "__main__":
    sys.exit(main())
