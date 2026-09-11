import os

def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(SCRIPT_DIR, "keystrokes.log")

log = open(log_path).read().strip()

print("Trying all 26 possible shifts...\n")
for shift in range(26):
    candidate = encrypt(log, -shift)
    print(f"Shift {shift:2d}:\n{candidate}\n")