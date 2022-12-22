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

# Returns a string first populated by the key letters and then is filled
# in with the rest of the ordered alphabet letters
def shift_alpha(key, alpha):
    arr = ""
    for char in key:
        arr += char
    for char in alpha:
        if char not in arr:
            arr += char
    return arr

box_list = shift_alpha(key, alpha)
box = [list(box_list[i:i+5]) for i in range(0, len(box_list), 5)]

"""
box equals a value of:
[['s', 'h', 'a', 'd', 'o'], ..., ['t', 'u', 'v', 'y', 'z']]
"""


