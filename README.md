Secure Password Generator
A cryptographically secure password generator that combines multiple entropy sources to create memorable, high-strength passwords using a word-based format.
Features

Cryptographic Security: Utilizes Python's secrets module for cryptographically secure random number generation
Multi-Source Entropy: Combines secure random bits, high-resolution timing, and user input for maximum unpredictability
SHA-384 Hashing: Processes entropy through robust cryptographic hashing
Memorable Format: Generates passwords in a word-symbol-symbol-word pattern for better usability
Customizable Wordlist: Uses external JSON wordlist for easy customization
Clipboard Integration: One-click copying to clipboard for convenience

Security Architecture
The generator employs a multi-layered approach to ensure cryptographic strength:

Primary Entropy: 128-bit cryptographically secure random number generation
Temporal Entropy: High-resolution nanosecond timing data
User Entropy: Additional randomness from user input
Cryptographic Processing: SHA-384 hashing of combined entropy sources
Seeded Generation: Uses hash output to seed final password construction

Installation
Prerequisites

Python 3.6 or higher
Required packages:
