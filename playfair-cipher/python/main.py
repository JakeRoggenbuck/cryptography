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

print(box)

# Takes in a digraph argument and returns the correct ciphertext digraph
def get_ciphertext(digraph: str) -> str:
    # We never include handling for empty plaintext in encrypt().
    if digraph == "":
        return

    rows = [0, 0]
    cols = [0, 0]
    # Used to break out of loop once both the row and columns are 
    # found for both chars.
    finished = [0, 0] 

    for row in box:
        for i in range(2):
            if row.__contains__(digraph[i]):
                rows[i] = box.index(row)
                cols[i] = row.index(digraph[i])
                finished[i] = 1
            if (finished[0] and finished[1]):
                break

    # Case one: Both in same row
    if (rows[0] == rows[1]):
        pass

    # Case two: Both in same column
    if (cols[0] == cols[1]):
        pass

    # Case three: Both in different rows and columns
    else:
        pass

    return rows, cols

print(get_ciphertext("oz"))

def encrypt(plaintext: str) -> str:
    plaintext = plaintext.replace(" ", "").lower()

    # If the plaintext is one character, a digraph does not exist. Create and return
    # ciphertext digraph using 'z' char as padding.
    if (len(plaintext) == 1):
        return box[alpha.index('z')][alpha.index(plaintext)]

    # At this point, len(plaintext) >= 2. Create the digraph list using 
    # only even pairs of letters. Handling for if plaintext is odd 
    # (ex. 7 letters) occurs on line 60.
    ciphertext = ""
    #digraphs = [plaintext[i] + plaintext[i + 1]
    #            for i in range(len(plaintext) - 1) if i % 2 == 0]

    # Populate 'ciphertext' string with ciphertext digraphs
    #for i in digraphs:
    #    ciphertext += sbox[alpha.index(i[1])][alpha.index(i[0])]

    # If the plaintext length is odd, add a new ciphertext digraph using the last
    # character of plaintext and the char 'z' as padding.
    #if (len(plaintext) % 2 == 1):
    #    ciphertext += sbox[alpha.index('z')][alpha.index(plaintext[-1])]

    return ciphertext
