#This is a simple implementation of the Caesar cipher decryption in Python.
#It takes an encrypted message and the original shift amount as input,
#and outputs the decrypted message#
def decrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65) #This line is the only difference from the encrypt function. It subtracts the shift instead of adding it to reverse the encryption process.
        else:
            result += char  # leave spaces/punctuation untouched
    return result

message = input("Message to decrypt: ")
key = int(input("Original shift amount (1-25): "))
print("Decrypted:", decrypt(message, key))