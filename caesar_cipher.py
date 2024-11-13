# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, add it as is
            result += char
    
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Get user input for message and shift
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

# Encrypt and decrypt the message
encrypted_message = encrypt(message, shift_value)
decrypted_message = decrypt(encrypted_message, shift_value)

# Display the results
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")