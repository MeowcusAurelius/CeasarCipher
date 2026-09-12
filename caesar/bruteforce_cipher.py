"""Print every possible Caesar decryption for an encrypted log file."""

#It reads the encrypted text from a log file named "keystrokes.log" located in the same directory as the script. 
#The script then prints out the decrypted text for each possible shift value from 0 to 25.
import os

def encrypt(text, shift):
    """Move letters by ``shift`` places while preserving other characters."""
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

# Build a path relative to this script so the program works from any folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# The encrypted log is created by the keylogging programs in the sibling folder.
log_path = os.path.join(SCRIPT_DIR, "..", "keylogging", "keystrokes.log")

# The file is opened for reading and closed automatically at the end of the block.
with open(log_path) as log_file:
    log = log_file.read().strip()

# A Caesar cipher has 26 possible shifts, including shift 0.
print("Trying all 26 possible shifts...\n")
for shift in range(26):
    # Decrypting by shift is the same as encrypting by negative shift.
    candidate = encrypt(log, -shift)
    print(f"Shift {shift:2d}:\n{candidate}\n")