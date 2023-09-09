# Vigénere's Cipher
# Created by Fer Cortés & Arantza Parra
# Date: 2023/09/08

# This code is a implementation of the Vigenere's Cipher.
        # It is a method of encrypting alphabetic text by
        # using alphabetic substitution.
# This particular code will read a txt file and decript it using the Vigenere's Cipher.
# The user must enter the name of the file and the program will return the decrypted text



from collections import Counter

# Function to save the deciphered text and the key to a file
def save_to_file(filename, key, decrypted_text):
    with open(filename, 'w') as f:
        f.write(f'Key: {key}\n')
        f.write('Decrypted Text:\n')
        f.write(decrypted_text)

# Return the most common element in the list.
'''This function determines the most frequent character in a given list.
Such a function is useful in deciphering, as in many languages, 
some characters appear more frequently and can be used as a hint 
to break the code. '''
def most_common_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else " "

# Decipher a single character using the given key
def decipher_char(char, key):
    shifted = alf.index(char) - key
    return alf[shifted % len(alf)]

# Decipher a list of characters
''' First, the function determines the most common 
    character in the list.
    Then, it makes the assumption that the most common character in the 
    ciphered text corresponds to a space in the plain text. 
    Then it calculates a shift value and uses it to decipher 
    the entire list of characters.'''

def decipher_list(lst):
    common_char = most_common_element(lst)
    assumed_space_shift = keyShift(common_char) - keyShift(" ")
    deciphered_list = [decipher_char(c, assumed_space_shift) for c in lst]
    return deciphered_list, assumed_space_shift

# Split the list into n sublists
def chunk_list(lst, n):
    return [lst[i::n] for i in range(n)]

# Merge the sublists into a single list
def merge_sublists(sublists):
    merged = []
    max_len = max(len(sublist) for sublist in sublists)
    
    for j in range(max_len):
        for sublist in sublists:
            if j < len(sublist):
                merged.append(sublist[j])
    return merged

if __name__ == "__main__":
    alf = list("abcdefghijklmnopqrstuvwxyz ")
    keyShift = alf.index

    with open("cipher2.txt", "r") as f:
        text = list(f.read().strip())

    n = 4
    sublists = chunk_list(text, n)
    
    deciphered_sublists = []
    key = ''

    for sublist in sublists:
        dec_sublist, sub_key = decipher_list(sublist)
        deciphered_sublists.append(dec_sublist)
        key += alf[sub_key % len(alf)]
    
    decrypted_text = ''.join(merge_sublists(deciphered_sublists))

    save_to_file('decrypted_output.txt', key, decrypted_text)

    # Save the results to a file
    print(f"The file 'decrypted_output.txt' has been created with key '{key}'.")
