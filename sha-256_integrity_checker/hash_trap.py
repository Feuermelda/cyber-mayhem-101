import hashlib
import os
import random
from pathlib import Path
import json
import time
from datetime import datetime
import sys


def save_to_log(typ, file_name):
    match typ:
        case 1: mod_type = "DELETED"
        case 2: mod_type = "MODIFIED"
        case 3: mod_type = "ADDED"
        case _: mod_type = "UNCHANGED"

    return f"{datetime.now()} {mod_type}: {file_name}"


mode = input("Type 'init' to set baseline, or press Enter to compare: ").strip()
eel_dir = Path("confidential")

if mode == "init":

    hash_dict = {}

    for file_path in eel_dir.glob("*"):

        if file_path.is_file():
            with open(file_path, "rb") as f:

                filedata = f.read()
                filehash = hashlib.sha256(filedata).hexdigest()
                hash_dict.update({file_path.name: filehash})

    with open("baseline_hashes.json", "w", encoding="utf-8") as f:
        json.dump(hash_dict, f, indent=4)

    print("Baseline hashes saved to baseline_hashes.json")

else:

    try:
        with open("baseline_hashes.json", "r", encoding="utf-8") as f:
            baseline = json.load(f)
            file_list = [f.name for f in eel_dir.glob("*") if f.is_file()]

    except FileNotFoundError:
        print("Sorry, no baseline hashes saved.\n")
        sys.exit()

    random_attacker = random.random()

    if random_attacker >= 0.75:
        random_file = random.randrange(0, len(file_list))
        target_file = file_list[random_file]
        path = f"confidential/{target_file}"
        if os.path.getsize(path) >= 20:
            with open(path, "r+b") as f:
                f.seek(13)
                f.write(b"This is an attack.")
        else:
            print(f"[!] Skipped editing {target_file}: too small.")

        random_file = random.randrange(0, len(file_list))
        os.remove(f"confidential/{file_list[random_file]}")
        attack_file = Path("confidential") / "attack_file.txt"
        attack_file.write_text("File added with worms and malware...")
        print("\nAttacker activated!\n")

    current = {}
    for file_path in eel_dir.glob("*"):
        if file_path.is_file():
            with open(file_path, "rb") as f:
                filedata = f.read()
                filehash = hashlib.sha256(filedata).hexdigest()
                current[file_path.name] = filehash

    print("Comparing file integrity...\n")
    time.sleep(5)

    for filename, old_hash in baseline.items():
        if filename not in current:
            msg = save_to_log(1, filename)

        elif current[filename] != old_hash:

            msg = save_to_log(2, filename)
        else:
            continue
        print(msg)
        with open("security_log.txt", "a", encoding="utf-8") as log:
            log.write(msg + "\n")
    for filename in current:
        if filename not in baseline:
            msg = save_to_log(3, filename)
            print(msg)
            with open("security_log.txt", "a", encoding="utf-8") as log:
                log.write(msg + "\n")
