"""
Teo Honda-Scully | 2022

Similar to the monoalphabetic table-substitution-cipher, this is another substitution cipher.
Although, instead of replacing every plaintext letter with its corresponding ciphertext letter,
this cipher replaces every plaintext digraph with its corresponding ciphertext digraph

Think of a standard 10x10 multiplication table. If I want to multiply '5' by '6', I find '5' on
either a row or a column label, and then I move down to the corresponding '6' row or column, both
of which intersect at the '30' value. 

For this digraph substitution, the row and column labels are alphabet letters instead of 1..10, 
and the values are the corresponding ciphertext digraphs.

For simplicity's sake, this will only handle lowercase alphabets.
"""

# Instead of each row/column label expressing "abcdef..", we can add disorder by
# shifting the labels, making the table less predictable. Ex: "abcdef.." -> "fghijk..""
shift_row = 4
shift_column = 17

alpha = "abcdefghijklmnopqrstuvwxyz"

def shift_alpha(alpha, shift) -> str:
    return alpha[shift:len(alpha)] + alpha[:shift]

sbox = [[shift_alpha(alpha, shift_column)[i] + (shift_alpha(alpha, shift_row)[j])
         for j in range(len(alpha))] for i in range(len(alpha))]

"""
sbox equals a value of:
[['jr', 'js', 'jt', 'ju', ...], ['kr', 'ks', 'kt', 'ku', ...], ... [...'in', 'io', 'ip', 'iq']]

Calling the 'BA' intersection of table should return: 'js' (col = 1, row = 0) -> (table[0][1])
"""

def encrypt(plaintext) -> str:
    # Force lowercase and strip spaces
    plaintext = plaintext.replace(" ", "").lower()

    # If the plaintext is one character, a digraph does not exist. Create and return
    # ciphertext digraph using 'z' char as padding.
    if (len(plaintext) == 1):
        return sbox[alpha.index('z')][alpha.index(plaintext)]

    # At this point, len(plaintext) >= 2. Create the digraph list using 
    # only even pairs of letters. Handling for if plaintext is odd 
    # (ex. 7 letters) occurs on line 60.
    ciphertext = ""
    digraphs = [plaintext[i] + plaintext[i + 1]
                for i in range(len(plaintext) - 1) if i % 2 == 0]

    # Populate 'ciphertext' string with ciphertext digraphs
    for i in digraphs:
        ciphertext += sbox[alpha.index(i[1])][alpha.index(i[0])]

    # If the plaintext length is odd, add a new ciphertext digraph using the last
    # character of plaintext and the char 'z' as padding.
    if (len(plaintext) % 2 == 1):
        ciphertext += sbox[alpha.index('z')][alpha.index(plaintext[-1])]

    return ciphertext


def decrypt(ciphertext) -> str:
    plaintext = ""

    # Ciphertext will always be even length and len >= 2. No need for special handling.
    digraphs = [ciphertext[i] + ciphertext[i + 1]
                for i in range(len(ciphertext) - 1) if i % 2 == 0]
    
    for i in digraphs:
        plaintext += sbox[alpha.index(i[1])][alpha.index(i[0])]
    
    return plaintext