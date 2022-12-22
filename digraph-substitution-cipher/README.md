### Digraph-substitution-cipher

Similar to the [monoalphabetic table-substitution-cipher](https://github.com/thondascully/cryptography/edit/master/table-substitution-cipher), this is another substitution cipher. Unlike the monoalphabetic table cipher, instead of replacing every plaintext letter with its corresponding ciphertext letter,
this cipher replaces every plaintext digraph with its corresponding ciphertext digraph.

### What does the digraph substitution cipher do?

Think of a standard 10x10 multiplication table. If I want to multiply `5` by `6`, I first find the `5` column label, and then I move down to the corresponding `6` row label. At this point, both the column and row will intersect at the `30` value. 

For a digraph substitution cipher, the row and column labels are alphabet letters instead of 1..10, and the values are the corresponding ciphertext digraphs.

_For simplicity's sake, this will only handle lowercase alphabets._

-----------------------

### Implementation

Instead of each row/column label expressing `abcdef..`, we can add disorder by shifting the labels, making the table less predictable. Ex: `abcdef..` -> `fghijk..`

```python 'ignore
shift_row = 17
shift_column = 9

alpha = "abcdefghijklmnopqrstuvwxyz"

# Shifts the alphabet over by `shift` amount. Loops overflow values to start.
def shift_alpha(alpha, shift) -> str:
    return alpha[shift:len(alpha)] + alpha[:shift]
```
```python 'ignore
sbox = [[shift_alpha(alpha, shift_column)[i] + (shift_alpha(alpha, shift_row)[j])
         for j in range(len(alpha))] for i in range(len(alpha))]
```

`sbox` is reflected below

![imgonline-com-ua-Negative-ze8WEjKSqFMEraD](https://user-images.githubusercontent.com/114739901/209051753-8035721e-d4e8-44cf-899c-eb8c39f51b95.jpg)
