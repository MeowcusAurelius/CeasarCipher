"""Guess the key for each encrypted log chunk using English frequencies."""

#It reads the encrypted text from a log file named "keystrokes.log" located in the same directory as the script. 
#The script then prints out the decrypted text for each possible shift value from 0 to 25.
from collections import Counter
import os

def decrypt(text, shift):
    """Move letters backwards by ``shift`` places to decrypt the text."""
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# The logger stores its output in the sibling keylogging folder.
LOG_FILE = os.path.join(SCRIPT_DIR, "..", "keylogging", "keystrokes.log")

# English letter percentages. E is common in English, but it is not always
# the most common letter in a short message.
ENGLISH_FREQUENCIES = {
    "E": 12.70, "T": 9.06, "A": 8.17, "O": 7.51, "I": 6.97,
    "N": 6.75, "S": 6.33, "H": 6.09, "R": 5.99, "D": 4.25,
    "L": 4.03, "C": 2.78, "U": 2.76, "M": 2.41, "W": 2.36,
    "F": 2.23, "G": 2.02, "Y": 1.97, "P": 1.93, "B": 1.49,
    "V": 0.98, "K": 0.77, "J": 0.15, "X": 0.15, "Q": 0.10,
    "Z": 0.07,
}

def chi_square_score(text):
    """Give lower scores to text whose letter counts look more English-like."""
    letters = [char for char in text if char.isalpha()]
    counts = Counter(letters)
    total = len(letters)
    if total == 0:
        return float("inf")
    # Chi-square compares observed counts with expected English counts.
    return sum(
        (counts[letter] - total * expected / 100) ** 2
        / (total * expected / 100)
        for letter, expected in ENGLISH_FREQUENCIES.items()
    )

# encrypted_local_keylogger.py writes one encrypted chunk per line.
with open(LOG_FILE) as log:
    chunks = [line.rstrip("\n") for line in log if line.strip()]

if not chunks:
    raise SystemExit("keystrokes.log contains no letters to analyze.")

for chunk_number, ciphertext in enumerate(chunks, start=1):
    # A rotating key means each line must be guessed independently.
    candidates = [
        (chi_square_score(decrypt(ciphertext, shift)), shift)
        for shift in range(26)
    ]
    _, guessed_key = min(candidates)
    print(f"Chunk {chunk_number}: guessed key {guessed_key}")
    print(decrypt(ciphertext, guessed_key))