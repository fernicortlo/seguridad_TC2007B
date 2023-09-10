# One time pad
# Created by Arantza Parra & Fernanda Cortés
# Date: 2023/09/09

# This code is a simple implementation of the One time pad cipher.
# It is a symetric key algorithm in which the key is used to encrypt and decrypt the message.
# The user must enter a plaintext and the code will return the encrypted text and the key used. 
# The key will be randomly generated.

# The alphabet used will be "abcdefghijklmnopqrstuvwxyz ", the space is included.
# This code uses the secrets module where some of the characters are non-printable characters.

import secrets

alphabet = 'abcdefghijklmnopqrstuvwxyz '

#Function to generate a random key
def generate_key(length):
    return ''.join(secrets.choice(alphabet) for i in range(length))

# Function to do the XOR operation berween the plaintext and the key
def xor(text, key):
    result = ""
    #xor_op = 0
    for i in range(len(text)):
        xor_op= ord(text[i]) ^ ord(key[i])
        result += chr(xor_op)
    return result

# Function to cipher the text 
def encrypt(text, key):
    return xor(text,key)


def main():
    with open("input.txt", "r") as f:
        text = f.read().strip()

    key = generate_key(len(text))
    ciphertext = encrypt(text, key)

    with open("OTP.txt", "w") as f:
        f.write(f'Key: {key}\n')
        f.write('Ciphertext:\n')
        f.write(ciphertext)

    print("The ciphertext and key have been saved to OTP.txt")

# Asks user if they want to decrypt the text
ask = input("Do you want to decrypt the text? (y/n): ")
if ask == "y":
    with open("OTP.txt", "r") as f:
        lines = f.readlines()
        key = lines[0].strip().split(": ")[1]
        ciphertext = lines[2]

    decrypt = xor(ciphertext, key)
    print("The decrypted text is:", decrypt)
elif ask == "n":
    print("Okay, bye!")
else:
    print("Invalid option! Please enter 'y' for yes or 'n' for no.")

main()

 