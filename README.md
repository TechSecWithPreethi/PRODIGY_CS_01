# PRODIGY_CS_01
Python Program to Encrypt and Decrypt Text using Caesar Cipher Algorithm 

# Description
This Python program implements the Caesar Cipher, a simple encryption technique used to encrypt and decrypt text by shifting the letters of the alphabet by a fixed number of positions. This code provides two functions, " encrypt and decrypt", which allow the user to encrypt a message with a specified shift and decrypt it back to its original form.

# What is Caesar Cipher?
The Caesar Cipher is one of the earliest and simplest methods of encryption, attributed to Julius Caesar, who used it to communicate securely with his generals. In a Caesar Cipher, each letter in the plaintext is shifted a certain number of positions down or up the alphabet. 

- For example, with a shift of 3, A becomes D, B becomes E, and so on. If a letter reaches the end of the alphabet, it wraps around (e.g., Z becomes C with a shift of 3).

# Why Use Caesar Cipher?
The Caesar Cipher is primarily used for educational purposes and as a foundation for understanding more complex encryption methods. It's useful for learning the basics of cryptography and how encoding and decoding of information work. While it’s not secure enough for modern encryption standards, it's a simple, hands-on introduction to the concept of ciphering and encryption keys.

# How the Code Works
1. Encrypt Function (encrypt):

    - This function takes a text and shift as inputs.
    - It loops through each character in the text:
    - Uppercase letters are shifted by converting them to their ASCII code, applying the shift, and then converting back to a character.
    - Lowercase letters follow a similar process.
    - Non-letter characters (like spaces and punctuation) are added to the result without modification.
    - Returns the encrypted text as result.

2. Decrypt Function (decrypt):

This function uses the encrypt function with a negative shift to reverse the encryption, effectively shifting characters back to their original positions.

3. User Input:

The user is prompted to enter a message and a shift value.
The message is then encrypted using the encrypt function and decrypted back to the original text using the decrypt function.

4. Output:

The program displays both the encrypted and decrypted messages.

# Use of This Code
This code is helpful for understanding how basic encryption works and can be used as a learning tool for encryption concepts. It's ideal for introductory cryptography exercises, as it demonstrates key ideas such as character manipulation, ASCII encoding, and the concept of a shift key for encoding messages.






