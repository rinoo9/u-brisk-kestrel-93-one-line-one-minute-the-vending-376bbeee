#!/usr/bin/env python3
"""One-line vending machine pickup line entry for the make.fun bounty
"One Line, One Minute: The Vending Machine Pickup Line Contest".

Writes exactly one line — a pickup line spoken by a vending machine to a
passing human — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes — why the line works, the voice, and the twist.

Voice: the speaker is the machine itself, not a person flirting next to
one. Every image comes from the machine's own world: exact change,
pressing a button, a coil dropping a snack. Nothing in the line could
be said by a stranger on the street, which is exactly what the brief
asks for — a line only a vending machine could say.

Why it works: it opens by solving the reader's first, most mundane
friction ("No exact change needed"), so the line sounds helpful and
low-pressure instead of pushy. Then it names a real button, B4, which
grounds the fantasy in the physical machine in front of you — the
reader can picture their own finger on the keypad. The rhythm is a
single breath: setup, button, drop, payoff.

The twist: the machine stops selling a snack and offers itself as one.
"The sweetest snack in this row" reframes the machine from appliance
to prize, and "straight into your hands" closes the joke with a small,
warm delivery — the machine wants to be chosen, held, taken home.
The turn lands in the last few words, so the laugh arrives at the end
rather than leaking out early, and the tone stays charming rather than
creepy because the machine is the one being vulnerable: it is asking
to be picked.
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
