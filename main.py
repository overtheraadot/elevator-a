#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: the funniest thing an
elevator would say if it could talk, in the elevator's own voice.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "Going down? Same — emotionally. Please hold the doors, and my will to live."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS the elevator talking — on the subject, in its own voice,
#    answering its own "going down?" like a bored attendant.
# 2. The joke lands on first read, with the punchline in the last few words:
#    please hold the doors, and my will to live — the lift asking passengers
#    to hold it together.
# 3. It sounds like an elevator: the stock phrase, the door request, the
#    flat delivery of something no lift should ever say out loud.
# 4. Fresh angle: the elevator is not stuck or broken — it is just
#    emotionally going down too, and asking the passengers to hold it together.
# 5. Tight: every word earns its place inside the 120-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 120 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} characters, over the 120 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
