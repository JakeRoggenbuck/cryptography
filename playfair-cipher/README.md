### Playfair cipher

The **playfair cipher**! This one is sort of like the [digraph substitution cipher](https://github.com/thondascully/cryptography/tree/master/digraph-substitution-cipher) in utilizing a table (this one's is 5x5) and multiple digraph substitutions, but this cipher has a few more rules. Unlike the digraph substitution cipher mentioned above, this one does not have a ciphertext digraph intersection value based on two inputted label points from a plaintext digraph. The playfair cipher instead shifts isolated digraph characters up, down, or diagonally in the matrix according to the digraph classification.

For starters, this cipher has a [key](https://en.wikipedia.org/wiki/Key_(cryptography))!

### What is a key?

In cryptography, a key is typically a string of characters used within an algorithm so that the output appears random

### Playfair method

The matrix of this cipher has no labels and is a 25 letter list wrapped into a 5x5 matrix. If the key is `shadow`, the first six elements of the list will be `s`, `h`, `a`, `d`, `o`, `w`, where the `w` wraps around to the second row while the rest lies in the first row.

After the key is finished populating the beginning of the list, the rest of the list will be filled with the leftover alphabet letters in order. In other words, the seventh element will be `b`. The eighth `c`. The ninth `e`.

<table>
<tr><th>6</th><th>25</th></tr>
<tr><td>

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** |   |   |   |   |
| ⠀ |   |   |   |   |
| ⠀ |   |   |   |   |
| ⠀ |   |   |   |   |

</td><td>

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** | **b** | **c** | **e** | **f** |
| **g** | **i** | **j** | **k** | **l** |
| **m**| **n** | **p** | **q** | **r** |
| **t** | **u** | **v** | **y** | **z** |

</td></tr>
</table>

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

In the example below, the plaintext digraph is `br`. These two points serve as the diagonal vertices of a rectangle. The opposite two vertices, `f` and `n`, make up the ciphertext digraph. `b` points to `f` while `r` points to `n` for encryption substitution.

| s | h | a | d | o |
| :---: | :---: | :---: | :---: | :---: |
| **w** | ***`b`*** | **c** | **e** | ***`f`*** |
| **g** | **i** | **j** | **k** | **l** |
| **m**| ***`n`*** | **p** | **q** | ***`r`*** |
| **t** | **u** | **v** | **y** | **z** |

### Verification

The word `test` gets split into the digraphs `te` and `st`. The `t` and `e` characters are not in the same row nor in the same column, so the digraph abides by `case 3`. Forming a rectangle with `t` and `e` at diagonal vertices, the other two vertices are `y` and `w`, combining to form the ciphertext digraph. Alternatively, the `st` digraph's characters (`s` and `t`) lay in the same column, making its encryption abide by `case 2`. Each of the digraph's plaintext letters encrypts by shifting down one letter (or looping back to the top if there are no lower letters). 

```python 'ignore
string = "test"
print("Encrypting string %s... %s" % (string, encrypt(string)))
print("Decrypting string %s... %s" % (encrypt(string), decrypt(encrypt(string))))
```

Result:

<img width="635" alt="Screen Shot 2022-12-22 at 5 43 19 PM" src="https://user-images.githubusercontent.com/114739901/209254193-7c3a1c6c-b3d9-43dd-857d-56d03902eefc.png">

### Known variations:

- Instead of leaving out a letter like `x` from the matrix, some variations combine `i` and `j` into a single matrix cell. This means that all alpha letters can be used. In our cipher, we cannot encrypt a word with the letter `x`.
- Instead of adding a padding letter (`z`) in between repeating letters within a digraph, another variation just discard the second repeating letter altogether.
- Instead of adding a padding letter (`z`) in between repeating letters within a digraph, another variation appends the padded letter before the first repeated letter. This shifts every letter over by one, causing the repeating letters to not exist within the same digraph.

### Breaking the playfair cipher

As usual with substitution ciphers, frequency analysis is a valuable tool for breaking the playfair cipher. Matching frequent ciphertext pairs to common pairs in the english language. Another approach is brute forcing, which is possible given how small scale this alt sbox is.

# Test cases

```python 'ignore
string = "tests" 
```

<img width="634" alt="Screen Shot 2022-12-22 at 5 51 09 PM" src="https://user-images.githubusercontent.com/114739901/209254981-2d08e7d8-b751-4e2c-8f22-9581c971f451.png">


```python 'ignore
string = "hello world"  # repeating letter in digraph
```

<img width="632" alt="Screen Shot 2022-12-22 at 5 52 40 PM" src="https://user-images.githubusercontent.com/114739901/209255140-37ac45ea-cab0-4d69-bea8-cace24bd2647.png">

```python 'ignore
string = "my name is teo"
```

<img width="635" alt="Screen Shot 2022-12-22 at 5 56 26 PM" src="https://user-images.githubusercontent.com/114739901/209255590-e1c0066f-3495-436e-b7c5-9fdce2f6fcee.png">

```python 'ignore
string = "wOrd"
```

<img width="631" alt="Screen Shot 2022-12-22 at 5 57 20 PM" src="https://user-images.githubusercontent.com/114739901/209255677-efd6fae1-d4cc-4b91-a875-6209496388be.png">

```python 'ignore
string = "a"
```

<img width="632" alt="Screen Shot 2022-12-22 at 5 58 23 PM" src="https://user-images.githubusercontent.com/114739901/209255814-2cf05a51-1d0b-428b-bd3b-618f21574564.png">


```python 'ignore
string " b  "  # whitespaces
```

<img width="637" alt="Screen Shot 2022-12-22 at 5 58 51 PM" src="https://user-images.githubusercontent.com/114739901/209255921-fa717b8f-b2a3-4feb-b77c-e947ec15d887.png">




