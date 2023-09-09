# Vigénere's Cipher
# Created by Fer Cortés & Arantza Parra
# Date: 2023/09/08

# This code is a implementation of the Vigenere's Cipher.
# It is a method of encrypting alphabetic text by 
# using alphabetic substitution.

# Encryption formula: E_k(M_i) = (M_i + K_i) mod 26

# Decryption formula: D_k(C_i) = (C_i - K_i) mod 26

# The alphabet used will be "abcdefghijklmnopqrstuvwxyz ", 
# the space is included.

alf = list("abcdefghijklmnopqrstuvwxyz ")

# function to get the index of the key
def keyShift(key: str) -> int:
    return alf.index(key)

# First, we need to assign a number to each letter in the alphabet
letterToIndex = dict(zip(alf, range(len(alf))))
indexToLetter = dict(zip(range(len(alf)), alf))

def extend_key(text, key):
    extended_key = ''
    key_len = len(key)
    text_len = len(text)
    for i in range(text_len):
        extended_key += key[i % key_len]
    return extended_key

def encrypt(plaintext, key):
    encrypted = ''
    extended_key = extend_key(plaintext, key)

    for i in range(len(plaintext)):
        number = (letterToIndex[plaintext[i]] + letterToIndex[extended_key[i]]) % len(alf)
        encrypted += indexToLetter[number]

    return encrypted

def decrypt(cipher, key):
    decrypted = ''
    extended_key = extend_key(cipher, key)

    for i in range(len(cipher)):
        number = (letterToIndex[cipher[i]] - letterToIndex[extended_key[i]]) % len(alf)
        decrypted += indexToLetter[number]

    return decrypted

def main():
    # Print the menu
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    
    # Get user's choice
    choice = input("Enter your choice (1/2): ")

    # Validate the choice
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1 or 2")
        choice = input("Enter your choice (1/2): ")

    # Process based on the choice
    if choice == '1':
        # Get plaintext or ciphertext from the user
        text = input("Enter the text: ")
        # Get the key from the user
        key = input("Enter the key: ")  

        result = encrypt(text, key)
        print("Encrypted Text:", result)
    else:
        text = input("Enter the cipher: ")
        key = input("Enter the key: ")  
        result = decrypt(text, key)
        print("Decrypted Text:", result)


if __name__ == "__main__":
    main()
