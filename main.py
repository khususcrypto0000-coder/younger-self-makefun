#!/usr/bin/env python3
"""One-line entry for the make.fun bounty
"One Line to Your Younger Self" (u-boothlord-one-line-to-your-younger-self-22e97f76).

Writes exactly one line of text to /output/entry.txt (UTF-8).
Python standard library only. Deterministic: the same line every run.
"""

import os

# The entry: one line, spoken directly to the younger self.
ENTRY = (
    "Kid, the pencil you use to rewind the cassette is the same one "
    "you'll use to sign your first real contract \u2014 don't snap it in half."
)


def main():
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if len(text) > 200:
        raise SystemExit("entry must be at most 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
