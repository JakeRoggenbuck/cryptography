///
/// Jake Roggenbuck | 2022
///
use std::collections::HashMap;

const PLAINTEXT: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const CIPHERTEXT: &str = "OaTyqwGerPSApdfghjXUIlzxcZLMVWKuZvbCRnmYNoQBkisFDtJH";

/// Convert the input string into an encrypted string using the simple table cipher
/// Not for use in encryption outside of experiments
fn encrypt(input: String, table: HashMap<char, char>) -> String {
    let mut new = String::new();

    for c in input.chars() {
        if c == ' ' {
            new.push(' ');
        } else {
            new.push(*table.get(&c).unwrap_or(&' '));
        }
    }

    return new;
}

/// Create two maps for plaintext -> cipher and another for cipher -> plaintext
fn output_map(left: &str, right: &str) -> (HashMap<char, char>, HashMap<char, char>) {
    let mut one = HashMap::<char, char>::new();
    let mut two = HashMap::<char, char>::new();

    for (c1, c2) in left.chars().zip(right.chars()) {
        one.insert(c1, c2);
        two.insert(c2, c1);
    }

    return (one, two);
}

fn main() {
    let (encryption, decryption) = output_map(PLAINTEXT, CIPHERTEXT);

    // One way
    let input = "Hello I am Jake".to_string();
    let out = encrypt(input.clone(), encryption);

    // Then the other
    let fin = encrypt(out.clone(), decryption);

    // Check equality
    assert_eq!(input, fin);

    println!("'{}' -> '{}' -> '{}'", input, out, fin);
}
