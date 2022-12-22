"""
Teo Honda-Scully | 2022

The playfair cipher! This one is sort of like the digraph substitution cipher, except
there are a few more rules. Unlike the digraph substitution cipher, this one does not
have a ciphertext digraph intersection value based on the two inputted label points.

For starters, this cipher has a key!

See more about the implementation in the ../README.md file
"""

# By including a key, the output appears more random and less traceable
# than an ordered alphabet matrix.
key = "shadow"

# Exclude 'x' -> 25 letter alpha
alpha = "abcdefghijklmnopqrstuvwyz"  

sbox = [[(alpha[i:i+5]).split()] for i in range(0, len(alpha), 5)]
print(sbox)

print(alpha.split())