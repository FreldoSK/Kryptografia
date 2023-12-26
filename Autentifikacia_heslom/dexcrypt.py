import itertools
import string
from hashlib import md5
from base64 import b64encode

def crypt(passwd, salt):
    m = md5()
    m.update(passwd.encode('utf-8'))
    m.update(salt.encode('utf-8'))
    return b64encode(m.digest()).decode('utf-8')


shadow_entries = {}
with open(r"D:\projekty\VScode\Autentifikacia_heslom\shadow1.txt", "r") as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) == 3:
            username, salt, hashed = parts
            shadow_entries[username] = (salt, hashed)


found_passwords = {}

for username, (salt, hashed) in shadow_entries.items():
    for length in range(4, 6):  
        for passwd in itertools.product(string.ascii_letters + string.digits, repeat=length):
            generated_passwd = ''.join(passwd)
            print(f"Trying password: {generated_passwd} for user: {username}")  
            if crypt(generated_passwd, salt) == hashed:
                found_passwords[username] = generated_passwd
                break  
    if username not in found_passwords:
        print(f"No password found for {username}")


for user, passwd in found_passwords.items():
    print(f"Password for {user} is: {passwd}")
