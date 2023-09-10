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
    # ask for the file name
    file_name = input("Enter the name of the file with the text to encrypt with .txt extention: ")

    # read the content of the file
    with open(file_name, "r") as f:
        text = f.read()

    # generate a key
    key = generate_key(len(text))
    # encrypt the text
    ciphertext = encrypt(text, key)

    # write the ciphertext and the key to a file
    with open("OTP_CipherOutput.txt", "w") as f:
        f.write("Ciphertext:\n")
        f.write(ciphertext)
        f.write("\nKey:\n")
        f.write(key)

    print("The ciphertext and key have been saved to OTP_CipherOutput.txt")
main()


 