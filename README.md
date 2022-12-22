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

### [Digraph-substitution-cipher](digraph-substitution-cipher)

Similar to the monoalphabetic table-substitution-cipher, this is another substitution cipher. Unlike the monoalphabetic table cipher, instead of replacing every plaintext letter with its corresponding ciphertext letter, this cipher replaces every plaintext digraph with its corresponding ciphertext digraph.

### [Shift Cipher](shift-cipher)
Otherwise known as a caesar cipher, the **shift cipher** takes each letter in a plaintext message and shifts it by `n` indexes in the looping alphabet.

