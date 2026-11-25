#!/usr/bin/env python3
"""The 3 AM Excuse - a hardware wallet refuses to sign at 3 AM.

The wallet speaks for itself: it remembers the last 3 AM wake-up, keeps
its keys in bed, and makes the hour itself the joke. One line, under
200 characters, written to /output/entry.txt. Pure standard library.
"""

import os

LINE = (
    "Last time you woke me at 3 AM you spent 0.4 ETH on a frog JPEG. "
    "My keys stay in bed until sunrise \u2014 and until your judgment "
    "wakes up too."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, a single line with no trailing newline.
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
