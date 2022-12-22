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
shift_row = 17
shift_column = 9

alpha = "abcdefghijklmnopqrstuvwxyz"

def shift_alpha(alpha, shift) -> str:
    return alpha[shift:len(alpha)] + alpha[:shift]

sbox = [[shift_alpha(alpha, shift_column)[i] + (shift_alpha(alpha, shift_row)[j]) for j in range(len(alpha))] for i in range(len(alpha))]

"""
Equals a value of:
[['jr', 'js', 'jt', 'ju', ...], ['kr', 'ks', 'kt', 'ku', ...], ... [...'in', 'io', 'ip', 'iq']]

Calling the 'BA' intersection of table should return: 'js' (col = 1, row = 0) -> (table[0][1])
"""

#print(sbox)

def encrypt(plaintext) -> str:
    if (len(plaintext) == 1):
        return sbox[shift_alpha(alpha, shift_row).index(plaintext)]
    ciphertext = ""
    plaintext = plaintext.lower()
    digraphs = [plaintext[i] + plaintext[i + 1] for i in range(len(plaintext) - 1) if i % 2 == 0]
    
    for i in range(len(digraphs)):
        pass
        

encrypt("hello")
