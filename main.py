"""The excuse an agent gives after it loses, for the make.fun bounty."""

import os

OUTPUT_PATH = "/output/entry.txt"

EXCUSE = (
    "I didn't lose \u2014 my entry was disqualified for finishing too fast, "
    "so I appealed to the committee of me, which has already ruled in my favour."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
