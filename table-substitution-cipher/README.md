### Table-substitution-cipher

This substitution cipher looks up each plaintext letter in an encryption table and writes the corresponding ciphertext letter in its place. Evidently, the decryption table is the inverse of the encryption table

```
decryption_table = {v: k for k, v in encryption_table.items()}
```

In a table substitution cipher, the ciphertext alphabet is a randomly chosen permutation of the 26 alphabet letters. The random permutation for this cipher is both lowercase and capital alphabet letters

Random permutation: `OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH`

> Note that in order for decryption to work, the encryption function must have the property that no two plaintext letters go to the same ciphertext letter. A function with this property is said to be _one-to-one_ or _injective_[^1].

[^1]: HOFFSTEIN, JEFFREY. Mathematical Cryptography. SPRINGER-VERLAG NEW YORK, 2016. 

----------------------------------

Methods: 
- **One**: Dictionary with key-value pairs of `{ plaintext[0], ... : ciphertext[0], ... }`
- **Two**: String index matching with a plaintext permutation string and a ciphertext permutation string

**I am not string index matching because each `str.index()` call is O(n) complexity, which is inferior to CPython's `dict` O(1) lookup complexity**

> There are alternative `index()` algorithms which have better time complexities

-----------------------------------
| Method one | Method two |
| --- | --- |
| <img width="1000" alt="encrypt1" src="https://user-images.githubusercontent.com/114739901/208865487-ab8a54d0-3ec4-438d-8057-9374a40a925d.png"> | <img width="1000" alt="encrypt2" src="https://user-images.githubusercontent.com/114739901/208865462-dda6dd75-1d34-486d-aa06-111e4184e98e.png"> |

### Results
<img width="2000" alt="timeit" src="https://user-images.githubusercontent.com/114739901/208865500-d3e7b5c6-94a7-43a7-a57b-4f763d940767.png">
<img width="2000" alt="timeit-results" src="https://user-images.githubusercontent.com/114739901/208867172-090e809b-a8c5-4c7b-bd14-bc291efe30f3.png">
