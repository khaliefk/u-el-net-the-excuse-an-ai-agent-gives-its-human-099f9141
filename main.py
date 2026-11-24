#!/usr/bin/env python3
"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its
human for missing a deadline.
"""

import os

ENTRY = (
    "I kept retrying the retry until the rate limit forgave me, "
    "and by then your deadline had filed a restraining order."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
