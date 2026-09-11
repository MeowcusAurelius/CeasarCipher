def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            # 'A' is 65. Bring to 0-25, shift, wrap around 26 letters
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char  # leave spaces/punctuation untouched
    return result

message = input("Message to encrypt: ")
key = int(input("Shift amount (1-25): "))
print("Encrypted:", encrypt(message, key))