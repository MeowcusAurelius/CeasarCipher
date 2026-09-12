"""Educational example that prints keyboard events for ten seconds.

Only run this on a computer you own or have explicit permission to test.
"""

#It captures keystrokes for a specified duration and prints them to the console. 
#Note that this code is for educational purposes only and should not be used for malicious activities.
from pynput import keyboard

def on_press(key):
    """Print a normal character or the name of a special key."""
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # Special keys such as Enter and Shift do not have a .char value.
        print(f"Special key: {key}")

# Listener calls on_press whenever a key is pressed.
print("Logging for 10 seconds... type something!")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join(timeout=10)  # auto-stops after 10 seconds

print("Done capturing.")