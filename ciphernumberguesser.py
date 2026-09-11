#This script is a simple brute-force cipher decryption tool that attempts to decrypt a given text by trying all possible shifts in a Caesar cipher.
#It reads the encrypted text from a log file named "keystrokes.log" located in the same directory as the script. 
#The script then prints out the decrypted text for each possible shift value from 0 to 25.
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