#This is a simple implementation of the Caesar cipher in Python.
#It takes a message and a shift amount as input, and outputs the encrypted message.
#This definition encrypts the input text by shifting each letter by the specified amount, 
#wrapping around the alphabet if necessary. Non-alphabetic characters are left unchanged.
def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            # 'A' is 65. Bring to 0-25, shift, wrap around 26 letters
            # Then convert back to ASCII by adding 65. 
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char  # leave spaces/punctuation untouched
    return result

# Message and shift amount input
message = input("Message to encrypt: ")
key = int(input("Shift amount (1-25): "))
print("Encrypted:", encrypt(message, key))