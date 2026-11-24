"""One Letter for Your Day — entry program.

Writes exactly one letter, J, to /output/entry.txt.

The hidden word behind the letter is "juggling": a day spent keeping
five wallets, a dozen free mints and claims, a 15-minute price watch,
a claim window opening at 10:01 and a morning briefing all in the air
at once — and somehow not dropping any of them.

Standard library only. Deterministic: the same single byte every run.
No network, no input, no environment secrets.
"""

import os

LETTER = "J"
WORD = "juggling"  # the hidden word behind the letter


def main() -> None:
    # Guard the gate: the entry must be exactly one letter, A-Z, and the
    # initial of its hidden word. Fail loudly instead of shipping a bad file.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    if LETTER != WORD[0].upper():
        raise ValueError("letter must be the initial of its hidden word")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
