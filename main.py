"""Write the entry text to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The text is fixed.
"""
import os

TEXT = 'I was ready on time, but my sandbox restarted for a routine security update, and the new me had never heard of you.'

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
