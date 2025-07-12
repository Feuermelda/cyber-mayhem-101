# Login Lab: From Vulnerability to Security
A mini project to explore **insecure login** implementations, basic **password hashing**, and how attackers might **exploit** weak authentication systems.<br>
This project includes an intentionally flawed login system, a simple exploit, and a patched secure version using hashed passwords and **JSON-based storage**.

---

## Contents
- `vuln_login.py` - A vulnerable login system with logic flaws and insecure password handling
- `exploit_login.py` - A script that demonstrates how attackers could exploit the vulnerable system
- `patched_login.py` - A secure, hashed-password login system with proper user lookup
- `user.json` - A JSON file storing user credentials as SHA-256 hashes

---

## Requirements

- Python 3.6+
- No externial libraries required<br>
  (only uses built-in modules: `getpass`, `hashlib`, `json`)

---

## Features

- Insecure login logic (in `vuln_login.py`)
- Exploit simulation bypassing password checks
- Secure version with **SHA-256** password hashing and JSON-based credential store
- Emphasis on understanding common authentication mistakes

---

## Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/Feuermelda/vulnerable_login.git
   cd vulnerable_login
   ```
2. Run the vulnerable login script:
   ```bash
   python vuln_login.py
   ```
3. Try the exploit script:
   ```bash
   python exploit_login.py
   ```
4. Test the patched secure login:
   ```bash
   python patched_login.py
   ```

---

## Learning Outcomes

- Understand **common authentication pitfalls****** (e.g., default password access, empty strings, poor logic)
- Practice how exploits work in a safe environment
- Learn how to hash passwords using SHA-256
- Work with basic `json` for user data storage
- Gain insight into how login systems should **not** and **should** behave

---

## Future Expansion Ideas

- Add a registration system for new users
- Implement password salting for stronger security
- Limit login attempts or lock users out after repeated failures
- Store user data securely using `.pem` or encrypted storage
- Restrict usage of the login function if it's not run directly (e.g., `if __name__ == "__main__"`)
- Add command-line arguments for login attempts or account creation

---

## Notes

This project was created as part of my **Cyber Mayhem 101** learning path.<br>
It serves as a safe sandbox to understand **how login vulnerabilities are introduced and exploited** - and how to fix them!