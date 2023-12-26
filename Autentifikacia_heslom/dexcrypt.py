import itertools
import string
from hashlib import md5
from base64 import b64encode
from concurrent.futures import ThreadPoolExecutor, as_completed

def crypt(passwd, salt):
    m = md5()
    m.update(passwd.encode('utf-8'))
    m.update(salt.encode('utf-8'))
    return b64encode(m.digest()).decode('utf-8')

def attempt_passwords(username, salt, hashed):
    for length in range(4, 5):  
        for passwd in itertools.product(string.ascii_letters + string.digits, repeat=length):
            generated_passwd = ''.join(passwd)
            print(f"Trying password: {generated_passwd} for user: {username}")  
            if crypt(generated_passwd, salt) == hashed:
                return username, generated_passwd
    return username, None

shadow_entries = {}
with open(r".\Autentifikacia_heslom\shadow1.txt", "r") as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) == 3:
            username, salt, hashed = parts
            shadow_entries[username] = (salt, hashed)

found_passwords = {}

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(attempt_passwords, user, data[0], data[1]): user for user, data in shadow_entries.items()}
    for future in as_completed(futures):
        user, found_passwd = future.result()
        if found_passwd:
            found_passwords[user] = found_passwd
            print(f"Password found: {found_passwd} for user: {user}")
        else:
            print(f"No password found for {user}")


for user, passwd in found_passwords.items():
    print(f"Password for {user} is: {passwd}")
