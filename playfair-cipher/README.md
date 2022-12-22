### Playfair cipher

The **playfair cipher**! This one is sort of like the [digraph substitution cipher](https://github.com/thondascully/cryptography/tree/master/digraph-substitution-cipher), except there are a few more rules. Unlike the digraph substitution cipher, this one does not have a ciphertext digraph intersection value based on the two inputted label points.

For starters, this cipher has a [key](https://en.wikipedia.org/wiki/Key_(cryptography))!

### What is a key?

In cryptography, a key is typically a string of characters used within an algorithm so that the output appears random

### Playfair method

The matrix of this cipher has no labels and is a 25 letter list wrapped into a 5x5 matrix. If the key is `shadow`, the first six elements of the list will be `s`, `h`, `a`, `d`, `o`, `w`, where the `w` wraps around to the second row while the rest lies in the first row.

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** |   |   |   |   |
| ⠀ |   |   |   |   |
| ⠀ |   |   |   |   |
| ⠀ |   |   |   |   |

After the key is finished populating the beginning of the list, the rest of the list will be filled with the leftover alphabet letters in order. In other words, the seventh element will be `b`. The eighth `c`. The ninth `e`.

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** | **b** | **c** | **e** | **f** |
| **g** | **i** | **j** | **k** | **l** |
| **m**| **n** | **p** | **q** | **r** |
| **t** | **u** | **v** | **y** | **z** |

> Did you notice that the letter `x` is missing? That is because in a 5x5 matrix, one letter from the 26 letter alphabet will be missing! We are choosing `x` to fill this role.

### Matrix constraints / rules

- **Constraint one**: The plaintext (like the digraph cipher) is split into [digraphs](https://en.wikipedia.org/wiki/Digraph) (sets of two characters). If there is a standalone letter, a `z` is padded for the creation of a digraph.

- **Constraint two**: Two of the same letters cannot be used in the same digraph. For example, `llama` gets separated into `lz`, `la`, and `ma`. The `z` is inserted in between the two repeating letters previously existing in the same digraph.

> Note: A word such as `moo` is okay because this gets separated into the digraphs `mo` and `oz`, in which there are no repeating letters in the same pair.

### Encryption rules

There are a few rules (cases) for encryption as well:

- **Case 1**: Both plaintext digraph characters exist in the same row of the 5x5 matrix. For each letter in the digraph: the corresponding ciphertext letter is the letter to the right of the plaintext letter in the row. 

```python 'ignore
row = ['a', 'b', 'c', 'd', 'e']
encrypt('ac')  # returns 'bd'

# the row wraps around back into itself (index % 5).
encrypt('be')  # returns 'ca'
```

- **Case 2**: Both plaintext digraph characters exist in the same column of the 5x5 matrix.For each letter in the digraph: the corresponding ciphertext letter is the letter below the plaintex letter in the column. The same wrap around rule applies vertically.

```python 'ignore
matrix = [['a'], ['b'], ['c'], ['d'], ['e']]  # column -> abcde
encrypt('bc')  # return 'cd'
```

- **Case 3**: Neither of the above two cases apply. When this happens, form a rectangle with each plaintext letter serving as diagonal vertices. The two opposite vertices are the corresponding ciphertext letters.

In the example below, the plaintext digraph is `br`. These two points serve as the diagonal vertices of a rectangle. The opposite two vertices, `f` and `n`, make up the ciphertext digraph.

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** | ***`b`*** | **c** | **e** | ***`f`*** |
| **g** | **i** | **j** | **k** | **l** |
| **m**| ***`n`*** | **p** | **q** | ***`r`*** |
| **t** | **u** | **v** | **y** | **z** |

> `b` -> `f`  
> `n` -> `r`  

