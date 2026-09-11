from collections import Counter

def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

ciphertext = open("keystrokes.log").read().strip()

counts = Counter(ch for ch in ciphertext if ch.isalpha())
most_common_char = counts.most_common(1)[0][0]
guessed_key = (ord(most_common_char) - ord("E")) % 26

print("Most common encrypted letter:", most_common_char)
print("Guessed key:", guessed_key)
print("Best guess decryption:")
print(encrypt(ciphertext, -guessed_key))