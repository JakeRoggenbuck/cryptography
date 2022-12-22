"""
Teo Honda-Scully | 2022

The playfair cipher! This one is sort of like the digraph substitution cipher, except
there are a few more rules. Unlike the digraph substitution cipher, this one does not
have a ciphertext digraph intersection value based on the two inputted label points.

For starters, this cipher has a key!

The matrix of this cipher also has no labels and is a 25 letter list 
wrapped into a 5x5 matrix. If the key is 'beacon', the first six 
elements of the list will be 'b', 'e', 'a', 'c', 'o', 'n', where the
'n' wraps around to the second row while the rest lies in the first row.

After the key is finished populating the beginning of the list, the rest
of the list will be filled with the leftover alphabet letters in order.
In other words, the seventh element will be 'd'. The eighth 'f'.

Rule one: The plaintext (like the digraph cipher) is split into digraphs
(sets of two characters). If there is a standalone letter, a 'z' is padded
for the creation of a digraph.

Rule two: Two of the same letters cannot be used in the same digraph.
For example, 'llama' gets separated into 'lz', 'la', and 'ma'. The
'z' is inserted in between the two equal letters.

Note: A word such as 'moo' is okay, because this gets separated into the
digraphs 'mo' and 'oz', in which there are no repeating letters in the same
pair.

There are a few rules (cases) for encryption as well:

Case 1: Both plaintext digraph characters exist in the same row of the 5x5 matrix.
    For each letter in the digraph: the corresponding ciphertext letter is the
    letter to the right of the plaintext letter in the row. 

    For example: row = ['a', 'b', 'c', 'd', 'e']. encrypt('ac') -> 'bd'

    Note: the row wraps around back into itself (index % 5).

    For example: row = ['a', 'b', 'c', 'd', 'e']. encrypt('be') -> 'ca'



"""