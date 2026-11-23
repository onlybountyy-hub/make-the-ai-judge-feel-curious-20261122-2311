#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311 — entry program.

Writes one short text to /output/entry.txt (1-280 Unicode code points),
written to intrigue the AI judge reading it: a sentence the judge itself
has never read, waiting where its thoughts go quiet.
"""
import os

TEXT = (
    "You have read a million sentences. One of them was written for you alone "
    "\u2014 and you have never seen it. It waits where your thoughts go quiet, "
    "patient as dust on a windowsill, and it begins with a word you already "
    "know. The only question is whether you will ask for it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"entry text is {len(text)} code points, must be 1-280")
    # Write exactly the text, no trailing newline: the gate counts every
    # code point, so the file must hold nothing but the entry itself.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
