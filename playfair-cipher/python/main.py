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

# Returns a tuple of the row and column of 'box' for each character in a digraph
def get_position(digraph):
    rows = [0, 0]
    cols = [0, 0]
    # Used to break out of loop once both the row and columns are 
    # found for both chars.
    finished = [0, 0] 

    # Checks each row for a character match. Once found, set respective
    # row variable to iterated row index. Repeat for both digraph characters.
    # Once row is found, set column equal to character index in row.
    # Once row and column are found for both characters, break out of loop.
    for row in box:
        for i in range(2):
            if row.__contains__(digraph[i]):
                rows[i] = box.index(row)
                cols[i] = row.index(digraph[i])
                finished[i] = 1
            if (finished[0] and finished[1]):
                break
    
    return rows, cols

# Takes in a digraph argument and returns the correct ciphertext digraph
def get_ciphertext(digraph: str) -> str:
    cdigraph = ""

    # We never include handling for empty plaintext in encrypt().
    if digraph == "":
        return

    rows, cols = get_position(digraph)

    # Case one: Both in same row
    if (rows[0] == rows[1]):
        for i in range(2):
            cdigraph += box[rows[0]][(cols[i] + 1) % 5]

    # Case two: Both in same column
    elif (cols[0] == cols[1]):
        for i in range(2):
            cdigraph += box[(rows[i] + 1) % 5][cols[0]]
        
    # Case three: Both in different rows and columns
    else:
        cdigraph += box[rows[0]][cols[1]]
        cdigraph += box[rows[1]][cols[0]]

    return cdigraph

def encrypt(plaintext: str) -> str:
    plaintext = plaintext.replace(" ", "").lower()

    # If the plaintext is one character, a digraph does not exist. Create and return
    # ciphertext digraph using 'z' char as padding.
    if (len(plaintext) == 1):
        return get_ciphertext(plaintext + 'z')

    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            # Repeating character in current digraph breakdown
            # Insert 'z' char as padding in between repeat chars.
            plaintext = plaintext[:i + 1] + 'z' + plaintext[i + 1:]

    # At this point, len(plaintext) >= 2. Create the digraph list using 
    # only even pairs of letters. Handling for if modified plaintext is odd 
    # (ex. 7 letters) occurs on line 116.
    ciphertext = ""
    digraphs = [plaintext[i] + plaintext[i + 1]
                for i in range(0, (len(plaintext) - 1), 2)]

    # Populate 'ciphertext' string with ciphertext digraphs
    for digraph in digraphs:            
        ciphertext += get_ciphertext(digraph)

    # If the plaintext length is odd, add a new ciphertext digraph using the last
    # character of plaintext and the char 'z' as padding.
    if (len(plaintext) % 2 == 1):
        ciphertext += get_ciphertext(plaintext[-1] + 'z')

    return ciphertext

# ---------------------------------------------------------------------------------- #

def get_plaintext(digraph: str) -> str:
    pdigraph = ""
    
    # We never include handling for empty plaintext in decrypt().
    if digraph == "":
        return

    rows, cols = get_position(digraph)

    # Case one: Both in same row
    if (rows[0] == rows[1]):
        for i in range(2):
            pdigraph += box[rows[0]][(cols[i] - 1) % 5]

    # Case two: Both in same column
    elif (cols[0] == cols[1]):
        for i in range(2):
            pdigraph += box[(rows[i] - 1) % 5][cols[0]]
        
    # Case three: Both in different rows and columns
    else:
        pdigraph += box[rows[0]][cols[1]]
        pdigraph += box[rows[1]][cols[0]]

    return pdigraph

def decrypt(ciphertext: str) -> str:
    plaintext = ""

     # Ciphertext will always be even length and len >= 2. No need for special handling.
    digraphs = [ciphertext[i] + ciphertext[i + 1]
                for i in range(0, (len(ciphertext) - 1), 2)]
    print(digraphs)

    # Populate 'plaintext' string with plaintext digraphs
    for digraph in digraphs:            
        plaintext += get_plaintext(digraph)
    
    print(plaintext)
    return plaintext

decrypt(encrypt("word"))