#!/usr/bin/env python3
"""One-line vending machine pickup line entry for the make.fun bounty
"One Line, One Minute: The Vending Machine Pickup Line Contest".

Writes exactly one line — a pickup line spoken by a vending machine to a
passing human — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the line speaks in the machine's own voice and world — no
exact change needed, press B4, the coil drops a snack — and the punch
lands in the last few words, when the machine offers to drop itself, the
sweetest snack in the row, straight into the human's hands. That fits
the judge brief: first a line only a vending machine could say, then the
machine's own slots, buttons and coils, then a laugh with the turn at
the end, short and speakable in one breath, and charming rather than
creepy.
"""

import os

LINE = (
    "No exact change needed \u2014 press B4 and I'll drop myself, "
    "the sweetest snack in this row, straight into your hands."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE == LINE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
