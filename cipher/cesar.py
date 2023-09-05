# Ceasar's Cipher
# Created by Arantza Parra & Fer Cortés
# Date: 2023/09/05

# This code is a simple implementation of the Ceasar's Cipher. 
# It is a substitution cipher in which each letter in the plaintext is replaced 
# by a letter some fixed number of positions down the alphabet.
# The user must enter a text and a number to shift the alphabet.
# The program will return the encrypted text.

# The alphabet used will be "abcdefghijklmnopqrstuvwxyz ", the space is included.
# lowecase letters: 97 - 122
            # uppercase letters: 65 - 90
            # space: 32


# Function to encrypt the text using ASCII code
def cesars_cypher(text, shift, operation):
    string = "" # Empty string to store the encrypted text
    if operation == "1":
        # Loop to iterate over the text
        for i in range(len(text)):
            character = text[i] # Get the character in the position i
            # if the character is lowercase
            if character.islower():
                string += chr((ord(character) + shift - 97) % 26 + 97)
            # if the character is a space
            elif character == " ":
                string += chr(((123) + shift - 97 ) % 27 + 97)
            # Encrypt the character
            # lowercase z -> 122
            # 122 + 3 = 125
            # 125 - 97 = 28 % 26 = 2 + 97 = 99 -> lowercase c         
            # space j -> 32
            # 32 + 3 = 35
            # 35 - 32 = 3 % 26 = 3 + 32 = 35 -> space j
        print("The encrypted text is: ", string)
    elif operation == "2":
        for i in range(len(text)):
            character = text[i] # Get the character in the position i
            if character == chr(((123) + shift - 97 ) % 27 + 97):
                string += " "
            elif character.islower():
                string += chr((ord(character) - shift - 97) % 26 + 97)
        print("The deciphered text is: ", string) 

    return string

operation = input("Do you want to encrypt (1) or decrypt (2) the text? ")
text = input("Enter the text: ")
shift_value = int(input("Enter the Caesar cipher shift value (positive integer): "))
cesars_cypher(text, shift_value, operation)