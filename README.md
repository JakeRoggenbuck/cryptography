### Cryptography?
The methodology of concealing the content of messages. Originates from the Greek root word _kryptos_, which means _hidden_. The modern scientific study of crytography is sometimes referred to as _cryptology_[^1].

[^1]: HOFFSTEIN, JEFFREY. Mathematical Cryptography. SPRINGER-VERLAG NEW YORK, 2016. 

**Project progress**

- [ ] Table substitution cipher
- [ ] Digraph substitution cipher
- [ ] Playfair cipher
- [ ] Shift cipher
- [ ] Vigenere cipher
- [ ] Affine cipher
- [ ] Steganography
- [ ] Xor
- [ ] One-time pad + proof of perfect secrecy
- [ ] Information theory: entropy analysis
- [ ] Information theory: wordle solver
- [ ] Block cipher
- [ ] Stream cipher
- [ ] Data encryption standard
- [ ] Padding oracle attack
- [ ] Hashing
- [ ] MACs
- [ ] Rainbow table attack
- [ ] RSA
- [ ] Diffie-Hellman key exchange
- [ ] ElGamal
- [ ] Complexity theory
- [ ] Abstract algebra review
- [ ] Factorization
- [ ] Discrete log
- [ ] Decisional Diffie-Hellman assumption
- [ ] Primality testing
- [ ] Elliptic-curve cryptography
- [ ] Lenstra's elliptic-curve factorization
- [ ] Elliptic-curve digital signature algorithm
- [ ] RSA signature
- [ ] ElGamal signature
- [ ] Existential forgery
- [ ] Shortest Vector Problem (bounds)
- [ ] Fundamental domain of lattices
- [ ] Reduction of Closest Vector Problem to SVP
- [ ] Subset sum of cryptosystem
- [ ] NTRU encryption algorithm
- [ ] Ring Learning With Errors

### [Table-substitution-cipher](table-substitution-cipher)

This substitution cipher looks up each plaintext letter in an encryption table and writes the corresponding ciphertext letter in its place. Evidently, the decryption table is the inverse of the encryption table

```python ,ignore
decryption_table = {v: k for k, v in encryption_table.items()}
```

In a table substitution cipher, the ciphertext alphabet is a randomly chosen permutation of the 26 alphabet letters. The random permutation for this cipher is both lowercase and capital alphabet letters

Random permutation example: `OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH`

| plaintext | ciphertext |
| :---: | :---: |
| `a` | `O` |
| `b` | `a` |
| `c` | `T` |

> plaintext to ciphertext values like `O`, `a`, and `T` are chosen randomly (or by using a generator).

### [Digraph-substitution-cipher](digraph-substitution-cipher)

Similar to the monoalphabetic [table substitution cipher](https://github.com/thondascully/cryptography/tree/master/table-substitution-cipher), this is another substitution cipher. Unlike the monoalphabetic table cipher, this cipher replaces every plaintext digraph with its corresponding ciphertext digraph instead of replacing every plaintext letter with its corresponding ciphertext letter.

### [Playfair cipher](playfair-cipher)

The **playfair cipher**! This one is sort of like the [digraph substitution cipher](https://github.com/thondascully/cryptography/tree/master/digraph-substitution-cipher) in utilizing a table (this one's is 5x5) and multiple digraph substitutions, but this cipher has a few more rules. Unlike the digraph substitution cipher mentioned above, this one does not have a ciphertext digraph intersection value based on two inputted label points from a plaintext digraph. The playfair cipher instead shifts isolated digraph characters up, down, or diagonally in the matrix according to the digraph classification.

For starters, this cipher has a [key](https://en.wikipedia.org/wiki/Key_(cryptography))!

Additionally, this cipher has a [key](https://en.wikipedia.org/wiki/Key_(cryptography))! See more at the title link.

### [Shift Cipher](shift-cipher)
Otherwise known as a caesar cipher, the **shift cipher** takes each letter in a plaintext message and shifts it by `n` indexes in the looping alphabet.

