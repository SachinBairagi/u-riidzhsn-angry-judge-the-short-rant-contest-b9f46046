"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is fixed text: the judge compares rants
two at a time, so the entry is deterministic and byte-identical on
every run.
"""

import os

RANT = (
    "I have clicked every traffic light, bicycle and crosswalk on the "
    "internet, and this website still squints at me and says: prove "
    "you are human. I AM human. I burn toast. I have cried at a dog "
    "food advert. Meanwhile the actual robots are already inside, "
    "laughing, while I sit here identifying fire hydrants like it is "
    "a job interview for my own species."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(RANT) <= 400):
        raise ValueError(
            "rant must be 1 to 400 characters, got %d" % len(RANT)
        )
    if not RANT.strip():
        raise ValueError("rant must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
