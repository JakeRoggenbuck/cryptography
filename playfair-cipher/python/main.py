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
"""