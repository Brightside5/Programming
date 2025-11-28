import string
import random
import hashlib

# generate a random fixed-length password from a source string 
# usage: python password.py

source = string.ascii_letters + string.punctuation + string.digits

print(source)

pwd_chars = random.choices(source,k=15)

print("Chosen chars:", pwd_chars)

pwd_string = "".join(pwd_chars

print("Password:", pwd_string)

# you can extend this to hash your password for secure storage using hashlib
hash_function = hashlib.sha256()

pwd_hash = ""

print("SHA256 hash:", pwd_hash)
