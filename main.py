#!/usr/bin/env python3
"""One Word for the Boss.

One word describing the entrant's boss: parrot.

The boss who repeats your idea in the meeting as if it were his own,
and repeats the same buzzwords until they mean nothing. The program
keeps the word as a literal, checks it against the competition's own
gate at run time (UTF-8 text, 1 to 30 characters, exactly one word of
letters only, no whitespace at all), and only then writes it to
/output/entry.txt. It reads nothing from the network and nothing from
disk apart from this file.
"""

WORD = "parrot"

LOWER = 1
UPPER = 30


def gate_failures(word):
    failures = []
    if len(word) < LOWER or len(word) > UPPER:
        failures.append(
            "length %d outside %d-%d" % (len(word), LOWER, UPPER)
        )
    if not word.strip():
        failures.append("must not be only whitespace")
    if word.strip() != word:
        failures.append("must not start or end with whitespace")
    if any(ch.isspace() for ch in word):
        failures.append("must be exactly one word, no whitespace inside")
    if not word.isalpha():
        failures.append("must be a single word of letters only")
    return failures


def main():
    failures = gate_failures(WORD)
    if failures:
        for failure in failures:
            print("gate failed: " + failure)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
