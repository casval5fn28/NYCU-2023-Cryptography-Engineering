import hashlib

# MD5 hashes to crack
hash1 = "5f4dcc3b5aa765d61d8327deb882cf99"
hash2 = "5a105e8b9d40e1329780d62ea2265d8a"

# List of common passwords to use in the dictionary attack
common_passwords = [
    "password",
    "123456",
    "qwerty",
    "letmein",
    "monkey",
    "football",
    "abc123",
    "111111",
    "admin",
    "welcome",
    "password1",
    "sunshine",
    "master",
    "hottie",
    "flower",
    "123qwe",
    "access",
    "shadow",
    "696969",
    "555555",
    "trustno1",
    "cipher",
    "cryptography",
    "engineering",
    "computerscience",
]

# Iterate over the list of common passwords and compare their MD5 hashes to the target hashes
for password in common_passwords:
    # Compute the MD5 hash of the current password
    password_hash = hashlib.md5(password.encode()).hexdigest()

    # Compare the hash to the target hashes
    if password_hash == hash1:
        print(f"Found password for hash1: {password}")
    if password_hash == hash2:
        print(f"Found password for hash2: {password}")