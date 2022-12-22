### Table-substitution-cipher

This substitution cipher looks up each plaintext letter in an encryption table and writes the corresponding ciphertext letter in its place. Evidently, the decryption table is the inverse of the encryption table

```python ,ignore
decryption_table = {v: k for k, v in encryption_table.items()}
```

In a table substitution cipher, the ciphertext alphabet is a randomly chosen permutation of the 26 alphabet letters. The random permutation for this cipher is both lowercase and capital alphabet letters

Random permutation: `OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH`

> Note that in order for decryption to work, the encryption function must have the property that no two plaintext letters go to the same ciphertext letter. A function with this property is said to be _one-to-one_ or _injective_[^1].

[^1]: HOFFSTEIN, JEFFREY. Mathematical Cryptography. SPRINGER-VERLAG NEW YORK, 2016. 

----------------------------------

### Methods: 
- **One**: Dictionary with key-value pairs of `{ plaintext[0], ... : ciphertext[0], ... }`
- **Two**: String index matching with a plaintext permutation string and a ciphertext permutation string

**I am not string index matching because each `str.index()` call is O(n) complexity, which is inferior to CPython's `dict` O(1) lookup complexity**

> There are alternative `index()` algorithms which have better time complexities


**Method one:**

```python 'ignore
def encrypt1(plaintext) -> str:
    return ''.join(encryption[c] for c in plaintext)
```

**Method two:**

```python 'ignore
def encrypt2(user_input):
    text = ""
    for c in user_input:
        text += ciphertext[plaintext.index(c)]
    return text
```

### Results

```python 'ignore
import timeit
string = "hello world my name is teo"
print("Time for encrypt1: '%s'" % timeit.Timer(lambda: encrypt1(string)).timeit(1))
print("Time for encrypt2: '%s'" % timeit.Timer(lambda: encrypt2(string)).timeit(1))
```

<img width="2000" alt="timeit-results" src="https://user-images.githubusercontent.com/114739901/208867172-090e809b-a8c5-4c7b-bd14-bc291efe30f3.png">

### Breaking a table substitution cipher:

If the message is long enough, one can use [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) to determine each ciphertext letter's respective plaintext letter. If the message is not long, but multiple ciphertext messages are available, one can use [differential cryptanalysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis).

If there is only one message and it is short, there is no viable way to break this cipher.
