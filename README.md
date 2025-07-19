

# Secure Password Generator

A cryptographically secure password generator that combines multiple entropy sources to create memorable, high-strength passwords using a word-based format.

---

## Features

- **Cryptographic Security**  
  Uses Python's `secrets` module for true random number generation.

- **Multi-Source Entropy**  
  Blends secure random bits, high-resolution timing, and optional user input.

- **SHA-384 Hashing**  
  Applies strong cryptographic hashing to processed entropy.

- **Memorable Format**  
  Passwords are generated in a `word-symbol-symbol-word` format for better usability.

- **Customizable Wordlist**  
  Reads from a JSON wordlist, easily swappable or extendable.

- **Clipboard Integration**  
  Automatically copies the password to clipboard for quick use.

---

## Security Architecture

This generator uses a layered entropy system to maximize randomness and security:

1. **Primary Entropy** – 128-bit random value from `secrets.randbits()`
2. **Temporal Entropy** – Nanosecond precision timestamp using `time.perf_counter_ns()`
3. **User Entropy** – Optional input from the user
4. **Hashing** – All entropy sources are combined and passed through `hashlib.sha384`
5. **Password Construction** – Final password is assembled using the digest output

---

## Installation

### Prerequisites

- Python 3.6 or newer
- Required packages:  
  `secrets`, `time`, `hashlib`, `json`, `string`, `random`

### Setup

Clone this repository:

```bash
git clone https://github.com/jakub712/cryptographic-password-generator.git
cd cryptographic-password-generator

Run the script:

python3 password_generator.py

License

This project is licensed under the MIT License.
See the LICENSE file for full terms.


---

Let me know if you want me to write the actual `LICENSE` file too or help commit this README.
