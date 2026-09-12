# Caesar Cipher Project

This is a small learning project about Caesar ciphers and keyboard event
listeners. It is intended for practice with Python, not for hiding sensitive
information or monitoring people.

Only run the keyboard examples on a computer you own or have explicit
permission to test.

## What is a Caesar cipher?

A Caesar cipher replaces each letter with another letter a fixed distance away
in the alphabet. For example, with a shift of 3:

```text
A -> D    B -> E    X -> A
```

The alphabet wraps around after Z. Spaces, numbers, and punctuation are kept
unchanged. This is useful for learning, but it is not secure encryption because
there are only 26 possible keys.

## Folders and files

The project is split into two folders. `caesar/` contains the cipher lessons.
`keylogging/` contains the local keyboard-listener lessons.

### `caesar/encrypt.py`

Asks for a message and a shift from 1 to 25, then prints the encrypted message.

```bash
python caesar/encrypt.py
```

### `caesar/decrypt.py`

Asks for encrypted text and the original shift, then moves each letter back to
recover the message.

```bash
python caesar/decrypt.py
```

### `caesar/bruteforce_cipher.py`

Reads `keystrokes.log` and prints all 26 possible decryptions. This works
because a Caesar cipher has only 26 possible shifts. Look through the results
for the one that forms readable text.

```bash
python caesar/bruteforce_cipher.py
```

### `caesar/cipher_key_guesser.py`

Reads each line of `keystrokes.log` as a separate encrypted chunk. It tries all
26 keys and scores each result using typical English letter frequencies. A
lower score means the letter pattern looks more like English.

This is only a guess. Short messages may not contain enough letters for
frequency analysis to be reliable.

```bash
python caesar/cipher_key_guesser.py
```

### `keylogging/local_keylogger.py`

Uses the third-party `pynput` package to print key presses for ten seconds. A
special key such as Enter does not have a normal character, so the program
prints its name instead.

```bash
python keylogging/local_keylogger.py
```

### `keylogging/encrypted_local_keylogger.py`

Collects keyboard events and writes encrypted text to `keystrokes.log`. Every
15 seconds, the current buffer is saved as one line and a new random Caesar
key is selected for the next line.

`keylogging/key.txt` contains only the most recently selected key. It does not
contain the older keys, which is why `cipher_key_guesser.py` is useful for this
exercise. The encrypted log is stored at `keylogging/keystrokes.log`.

This program needs access to a graphical display. It may not work inside a
headless container or remote terminal.

## Set up locally

Run these commands in a terminal on your own computer. A VS Code terminal
inside a Codespace, SSH session, or dev container is remote and may not be able
to see your local keyboard or desktop.

First, check that Python is installed:

```bash
python3 --version
```

On Windows, use `py --version` if `python3` is not available.

Create a virtual environment in the project folder. A virtual environment is
an isolated place for this project's Python packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install `pynput`

With the virtual environment activated, install the keyboard-listener package:

```bash
python -m pip install pynput
```

Confirm that Python can find it:

```bash
python -c "import pynput; print('pynput is installed')"
```

Run all commands below from the project folder and keep the virtual
environment activated. If VS Code shows an import warning, select the Python
interpreter inside `.venv` with **Python: Select Interpreter**.

## Test everything

### 1. Test basic encryption and decryption

Run:

```bash
python caesar/encrypt.py
```

Use `HELLO WORLD` as the message and `3` as the shift. The result should be
`KHOOR ZRUOG`.

Then run:

```bash
python caesar/decrypt.py
```

Enter `KHOOR ZRUOG` and `3`. The result should be `HELLO WORLD` again.

### 2. Test brute force and key guessing

These programs read `keylogging/keystrokes.log`, so they need an existing log
file. After completing the keyboard test below, run:

```bash
python caesar/bruteforce_cipher.py
python caesar/cipher_key_guesser.py
```

The brute-force program prints all 26 possibilities. The key guesser prints
one best guess per 15-second chunk. Compare the outputs with the text you
typed. Guesses can be wrong when a chunk is very short.

### 3. Test the local keyboard listener

On a local computer with an active desktop session, run:

```bash
python keylogging/local_keylogger.py
```

Type a short, harmless test message in another application. The program runs
for ten seconds and prints the keys it receives. Do not test this on another
person's computer.

### 4. Test the encrypted keyboard listener

Run:

```bash
python keylogging/encrypted_local_keylogger.py
```

Type a harmless test message and wait at least 15 seconds so one chunk is
written. Press `Esc` to stop. You should then see these generated files:

```text
keylogging/keystrokes.log
keylogging/key.txt
```

The log contains encrypted text. Each line is one chunk with its own random
key. The key guesser can estimate the keys without using `key.txt`.

Finally, run the two analysis programs from step 2.

### Troubleshooting

- `No module named pynput`: activate `.venv` and run `python -m pip install pynput`.
- `failed to acquire X connection`: run the keyboard program locally in a graphical desktop session, not in a headless container.
- The analysis tools cannot find the log: run the encrypted listener first, or check that `keylogging/keystrokes.log` exists.
- The key guess is incorrect: type a longer test message. Frequency analysis is unreliable with only a few letters.

## Suggested learning order

1. Run `caesar/encrypt.py` with a short message.
2. Use the same shift with `caesar/decrypt.py`.
3. Try `caesar/bruteforce_cipher.py` and compare all 26 results.
4. Read the functions and change one small part at a time.
5. Study the keyboard examples only in an approved test environment.
