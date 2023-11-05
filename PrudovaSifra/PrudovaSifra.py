import os

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
        print(f"File with name '{name}' was not found!")
    return memory, count

def process(passwd, plain_text, count):
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
    return process(passwd, plain_text, count)

def decrypt(passwd, cipher_text, count):
    return process(passwd, cipher_text, count)

def count_alphanumeric_chars(data):
    counter = 0
    total_chars = len(data)
    for byte in data:
        char = chr(byte)
        if char.isalnum():
            counter += 1
    return float(counter) / total_chars * 100
    

def main():
    input_filename = "./text3_enc.txt"
    max_counter = 0
    best_passwd = ""
    combinations = []

    #input_text, count = read_file(input_filename, MAX_TEXT_SIZE)
    #result = decrypt("555555", input_text, count)
    #print(result.decode("utf-8"))


    for number in range(100000, 1000000):
        passwd = str(number)
        input_text, count = read_file(input_filename, MAX_TEXT_SIZE)

        if count > 0:
            result = decrypt(passwd, input_text, count)
            counter = count_alphanumeric_chars(result)

            

            combinations.append((passwd, counter))

            if counter > max_counter:
                max_counter = counter
                best_passwd = passwd

    print(f"Best combination: {best_passwd}, number of alpha/numeric chars: {max_counter:.2f}")




if __name__ == "__main__":
    main()

