"""
Teo Honda-Scully | 2022

Method: Dictionary with key-value pairs of `plaintext`: `ciphertext`
I am lazy, so I will populate the keys and pairs from two alphabet strings (one unordered)

I am not using string index matching because each `str.index()` call is O(n) complexity.
"""

plaintext = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
ciphertext = "OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH " 
encryption = dict(zip(list(plaintext), list(ciphertext)))
decryption = dict(zip(list(ciphertext), list(plaintext)))

def encrypt(plaintext):
    plaintext = plaintext.replace(" ", "")
    return ''.join(encryption[c] for c in plaintext)

def decrypt(ciphertext):
    return ''.join(decryption[c] for c in ciphertext)