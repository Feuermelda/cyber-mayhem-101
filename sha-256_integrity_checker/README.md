# SHA-256 Integrity Checker
A **lightweight integrity monitoring** script designed for digital forensics and file tampering detection.<br>
It uses **SHA-256** hashing to create a trusted baseline and compare future file states, helping detect unauthorized changes.

## Requirements
- Python 3.x
- Standard libraries: `hashlib`, `os`, `random`, `json`, `time`, `datetime`, `pathlib`, `sys`

## Features
- Create a secure hash baseline of files in a directory
- Detect deleted, modified, and newly added files
- Simulate attacker behavior with randomized tampering
- Log all detected changes to a `security_log.txt` file

## Usage
1. Create a folder and add `.txt` files
2. Run the script with:
   
   ```bash
   python hash_trap.py
   ```
3. Type `init` to create the baseline<br>
   OR<br>
   Press Enter to compare current state against baseline and simulate an attack

## Learning Outcomes
- Understand how cryptographic hashes detect file tampering
- Learn how attackers might stealthily alter or delete files
- Practice logging, hashing, and file manipulation in Python