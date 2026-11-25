#!/usr/bin/env python3
"""The 3 AM Excuse - a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.
Pure standard library.
"""

import os

LINE = (
    "Last time you woke me at 3 AM you bought a frog JPEG for 0.4 ETH. "
    "My keys are staying in bed \u2014 come back when the sun, and your "
    "judgment, are up."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
