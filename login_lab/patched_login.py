from hashlib import sha256
from getpass import getpass
import json


def secure_login(username, password):

    if not password:
        return "Password rejected.\n"

    password_bytes = password.encode()

    password_hash = sha256(password_bytes).hexdigest()

    with open("user.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        users = data["users"]

        stored_hash = users.get(username)
        if stored_hash:
            if stored_hash == password_hash:
                return "Login successful.\n"
            else:
                return "Wrong password.\n"
        else:
            return "No user found.\n"


if __name__ == "__main__":

    usern = input("Please enter your username:\n").strip()
    passw = getpass("Please enter your password:\n").strip()

    print(secure_login(usern, passw))
