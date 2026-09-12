"""Ask for a message and encrypt it with a Caesar cipher."""

# A Caesar cipher moves every letter by the same number of places.
#It takes a message and a shift amount as input, and outputs the encrypted message.
#This definition encrypts the input text by shifting each letter by the specified amount, 
#wrapping around the alphabet if necessary. Non-alphabetic characters are left unchanged.
def encrypt(text, shift):
    """Return ``text`` with each letter moved forward by ``shift`` places."""
    result = ""
    for char in text.upper():
        if char.isalpha():
            # ord() gives A the number 65. Subtracting 65 changes A-Z to 0-25.
            # % 26 wraps Z back around to A when the shift goes past Z.
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            # Spaces, numbers, and punctuation do not need to be encrypted.
            result += char
    return result

# Get the two pieces of information needed by the program.
message = input("Message to encrypt: ")
key = int(input("Shift amount (1-25): "))
print("Encrypted:", encrypt(message, key))