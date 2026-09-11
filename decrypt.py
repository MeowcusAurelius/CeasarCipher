def decrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char  # leave spaces/punctuation untouched
    return result

message = input("Message to decrypt: ")
key = int(input("Original shift amount (1-25): "))
print("Decrypted:", decrypt(message, key))