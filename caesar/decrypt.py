"""Ask for encrypted text and reverse a Caesar cipher."""

# Decryption moves letters backwards by the same number used for encryption.
#It takes an encrypted message and the original shift amount as input,
#and outputs the decrypted message#
def decrypt(text, shift):
    """Return ``text`` with each letter moved backwards by ``shift`` places."""
    result = ""
    for char in text.upper():
        if char.isalpha():
            # Subtracting the key reverses the addition performed during encryption.
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            # Keep spaces, numbers, and punctuation readable.
            result += char
    return result

# Ask for the encrypted message and the original key.
message = input("Message to decrypt: ")
key = int(input("Original shift amount (1-25): "))
print("Decrypted:", decrypt(message, key))