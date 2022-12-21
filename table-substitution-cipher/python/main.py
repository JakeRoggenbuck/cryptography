import time

"""
Teo Honda-Scully | 2022

Method: Dictionary with key-value pairs of `plaintext`: `ciphertext`
I am lazy, so I will populate the keys and pairs from two alphabet strings (one unordered)

I am not using string index matching because each `str.index()` call is O(nm) complexity.
"""

plaintext = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
ciphertext = "OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH " 
encryption = dict(zip(list(plaintext), list(ciphertext)))
decryption = dict(zip(list(ciphertext), list(plaintext)))

type_input = ""
user_input = ""

def encrypt(plaintext):
    return ''.join(encryption[c] for c in plaintext)

def decrypt(ciphertext):
    return ''.join(decryption[c] for c in ciphertext)

print("\nWelcome to the table substitution cipher tool! Type 'q' to quit\n")

while (type_input != 'q'):
    type_input = input("Type 'e' to encrypt\nType 'd' to decrypt\n\n > ")
    if (type_input == 'e'):
        user_input = input("Enter plaintext: ")
        print(f'\n{encrypt(user_input)}\n')
        time.sleep(1)
    if (type_input == 'd'):
        user_input = input("Enter ciphertext: ")
        print(f'\n{decrypt(user_input)}\n')
        time.sleep(1)