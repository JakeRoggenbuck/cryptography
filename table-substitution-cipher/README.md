### Table substitution cipher

This substitution cipher looks up each plaintext letter in an encryption table and writes the corresponding ciphertext letter in its place. Evidently, the decryption table is the inverse of the encryption table

```python ,ignore
decryption_table = {v: k for k, v in encryption_table.items()}
```

In a table substitution cipher, the ciphertext alphabet is a randomly chosen permutation of the 26 alphabet letters. The random permutation for this cipher is both lowercase and capital alphabet letters

Random permutation: `OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH`

| plaintext | ciphertext |
| :---: | :---: |
| `a` | `O` |
| `b` | `a` |
| `c` | `T` |

> plaintext to ciphertext values like `O`, `a`, and `T` are chosen randomly (or by using a generator).

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

### Verifying that **Method one** is better

```python 'ignore
import timeit
string = "hello world my name is teo"
print("Time for encrypt1: '%s'" % timeit.Timer(lambda: encrypt1(string)).timeit(1))
print("Time for encrypt2: '%s'" % timeit.Timer(lambda: encrypt2(string)).timeit(1))
```

<img width="2000" alt="timeit-results" src="https://user-images.githubusercontent.com/114739901/208867172-090e809b-a8c5-4c7b-bd14-bc291efe30f3.png">

### Verification:

```python 'ignore
string = "hello"
print("Encrypting string %s... %s" % (string, encrypt(string)))
print("Decrypting string %s... %s" % (encrypt(string), decrypt(encrypt(string))))
```

Result:

<img width="633" alt="Screen Shot 2022-12-23 at 9 32 10 PM" src="https://user-images.githubusercontent.com/114739901/209422983-2e6d2f9f-b2cf-40bb-b962-bacca1e07fdc.png">


### Breaking a table substitution cipher:

If the message is long enough, one can use [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) to determine each ciphertext letter's respective plaintext letter. If the message is not long, but multiple ciphertext messages are available, one can use [differential cryptanalysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis).

If there is only one message and it is short, there is no viable way to break this cipher.

# Test cases

```python 'ignore
string = "hello world"
```

<img width="639" alt="Screen Shot 2022-12-23 at 9 36 49 PM" src="https://user-images.githubusercontent.com/114739901/209423049-0f0d59b0-61e9-4ae5-9111-98a9abf00180.png">

```python 'ignore
string = "  from Teo  "
```

<img width="635" alt="Screen Shot 2022-12-23 at 9 37 59 PM" src="https://user-images.githubusercontent.com/114739901/209423069-91d01935-1207-413b-b804-9f573365b4a0.png">

```python 'ignore
string = "'"
```

<img width="629" alt="Screen Shot 2022-12-23 at 9 41 28 PM" src="https://user-images.githubusercontent.com/114739901/209423141-7328a521-3b27-4379-b565-422fdc16e563.png">
