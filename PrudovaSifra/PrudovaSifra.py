import os

MODE_ENCRYPT = 0
MODE_DECRYPT = 1
MAX_TEXT_SIZE = 10000

rc4_s = [i for i in range(256)]

rc4_i = 0
rc4_j = 0

def get_key(passwd):
    rc4_k = []
    while len(rc4_k) < 256:
        for char in passwd:
            rc4_k.append(ord(char))
        rc4_k.append(0) 
    return rc4_k


def rc4_init(key):
    global rc4_s
    rc4_s = [i for i in range(256)]

    j = 0
    for i in range(256):
        j = (j + rc4_s[i] + key[i]) % 256
        rc4_s[i], rc4_s[j] = rc4_s[j], rc4_s[i]

    global rc4_i
    global rc4_j
    rc4_i = 0
    rc4_j = 0

def rc4_rand():
    global rc4_s
    global rc4_i
    global rc4_j
    rc4_i = (rc4_i + 1) % 256
    rc4_j = (rc4_j + rc4_s[rc4_i]) % 256
    rc4_s[rc4_i], rc4_s[rc4_j] = rc4_s[rc4_j], rc4_s[rc4_i]

    t = (rc4_s[rc4_i] + rc4_s[rc4_j]) % 256
    return rc4_s[t]

def read_file(name, max_size):
    count = 0
    memory = None
    try:
        with open(name, "rb") as stream:
            memory = stream.read(max_size)
            count = len(memory)
    except FileNotFoundError:
        print(f"Nepodařilo se načíst soubor '{name}'!")
    return memory, count

def write_file(name, memory, count):
    try:
        with open(name, "wb") as stream:
            stream.write(memory[:count])
    except IOError:
        print(f"Nepodařilo se zapsat soubor '{name}'!")

def process(passwd, plain_text, count, mode):
    key = get_key(passwd)
    rc4_init(key)

    result = bytearray(count)

    for i in range(count):
        p = plain_text[i]
        r = rc4_rand()
        c = p ^ r
        result[i] = c

    return result

def encrypt(passwd, plain_text, count):
    return process(passwd, plain_text, count, MODE_ENCRYPT)

def decrypt(passwd, cipher_text, count):
    return process(passwd, cipher_text, count, MODE_DECRYPT)

def main():
    mode = MODE_DECRYPT
    passwd = "123456"
    input_filename = "./text1_enc.txt"
    output_filename = "desifrovanie.txt"

    input_text, count = read_file(input_filename, MAX_TEXT_SIZE)
    if count == 0:
        print("Vstupní text je prázdný!")
        return

    if mode == MODE_ENCRYPT:
        result = encrypt(passwd, input_text, count)
    elif mode == MODE_DECRYPT:
        result = decrypt(passwd, input_text, count)

    write_file(output_filename, result, count)

if __name__ == "__main__":
    main()
