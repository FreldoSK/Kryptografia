import math
import random
import time

# Prelomenie RSA sifrovania

# Pre vypocet inverzenho prvku cez rozsireny Euklidov algoritmus
def egcd(a, b):
    u0, u1, v0, v1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    return  a, u0, v0

# Pre vypocet inverzneho prvku modulo
def modInverse(a, n):
    gcd, u, v = egcd(a, n)
    if gcd == 1:
        return u % n

# Prelomenie verejneho kluca, "uhadnut" prvocisla p a q, z ktorych bolo vypocitane n
# Pre male to nie je problem pomocou faktorizacie s postupnym delenim
def factorize(n):
    result = []
    counter = 0 # pre 1. 1321950 pre 2.1637176
    i = 2
    while (n > 1):
        j = 0;
        while (n % i == 0):
            n = n / i
            j = j + 1
        if (j > 0):
            result.append((i,j))
            print("Opakovany pri: ", counter," cislo: ",result,"\n")
        i = i + 1
        counter += 1
    print("Opakovany pri: ", counter,"\n")
    return result


# Funkcia pre urychenie pocitanie faktorizacie pre cisla vacie ako 10^19, pre 3. ulohu RSA
def factorize_via_6k_long_numbers(n):
    factors = []
    counter = 0 # max 272862
    start_inter= (330* int(n**0.33) -1)
    for i in range( start_inter , int(n**0.5) + 1):
        j = 0
        nasob = 6*i
        if n %(nasob -1) ==0 and (nasob -1) > 3 :
            if (n % (nasob - 1) == 0):
                n //= (nasob - 1)
                factors.append((nasob - 1))
                j +=1
            elif (n % (nasob + 1) == 0):
                n //= (nasob + 1)
                factors.append((nasob + 1))
                j +=1
        counter += 1 # increment the counter every time the loop iterates
        if j > 0:
            break
    if n > 1:
        factors.append(n)
    print("Opakovany pri: ", counter, "\n")
    return factors


# Funkcia pre pocitanie faktorizacie cez 6k +-1, boj proti log hodnoty
def factorize_via_6k(n):
    factors = []
    counter = 0 
    for i in range(2, int(n**0.5) + 1):
        j = 0
        nasob = 6*i
        if n %(nasob -1) ==0 and (nasob -1) > 3 :
            if (n % (nasob - 1) == 0):
                n //= (nasob - 1)
                factors.append((nasob - 1))
                j +=1
            elif (n % (nasob + 1) == 0):
                n //= (nasob + 1)
                factors.append((nasob + 1))
                j +=1

        elif n % i == 0 and i < 4:
            if i ==2:
                j =1
            elif i ==3:
                j = 1
            if j >0:
                n //= i
                factors.append(i)

        counter += 1
        if j > 0:
            break
    if n > 1:
        factors.append(n)
    print("Opakovany pri: ", counter, "\n")
    return factors

# hladanie len po odmocninu s n
def factorize_via_sqrt(n):
    counter = 0 
    factors = []
    n_max = int(n**0.5) + 1
    for i in range(2, n_max):
        j = 0
        while n % i == 0:
            factors.append(i)
            n //= i
            j +=1
            print("Opakovany pri: ", counter)
        counter += 1
        if j > 0:
            break
    if n > 1:
        factors.append(n)
    print("Opakovany pri: ", counter, "\n")
    return factors

"""
Uloha RSA
1. n = 2164267772327; e = 65537; y = 1325266873785;
2. n = 16812615098258879; e = 65537; y = 1990249581724467;
3. n = 181052234309092978339; e = 65537; y = 147885702766350471578;
4. n = 1327612780145399205245813; e = 65537; y = 1075593273482743198269527;
5. n = 329897251897125970254396723194243; e = 65537; y = 22712629296843271867140518185260;
6. n = 26845416039893360305516015851501077574841; e = 65537; y = 6820997247850432766042868007364587250604;
7. n = 2146776870009792253322117406137065611833216495831; e = 65537; y = 604615692674313046352476676786807225671015935385;
"""


if __name__ == '__main__':

    # ------ ulohy 1. a 2. cez funkciu -> factorize_via_6k(n); uloha 3. cez funkciu -> factorize_via_6k_long_numbers(n);
    prvo_cis = [ 2164267772327, 16812615098258879,  181052234309092978339,  1327612780145399205245813, 329897251897125970254396723194243,
                    26845416039893360305516015851501077574841, 2146776870009792253322117406137065611833216495831 ]

    # 1. 2164267772327 # 2. 16812615098258879 # 3. 181052234309092978339
    # 4. 1327612780145399205245813  = 1 065807 076247 × 1 245640 800979
    # 5. 329897251897125970254396723194243  = 16548 342710 737441 × 19935 364988 729123
    # 6. 26845416039893360305516015851501077574841  = 154 456071 032310 651803 × 173 806156 407264 626747
    # 7. 2146776870009792253322117406137065611833216495831  = 1 189877 692142 508366 049463 × 1 804199 611595 608193 523937

    # --------- https://www.alpertron.com.ar/ECM.HTM # tato stranka ti vie vypocitat rozklad

    # 4. 1327612780145399205245813                  = 1065807076247 × 1245640800979
    # 5. 329897251897125970254396723194243              = 16548342710737441 × 19935364988729123 toto je s tadial
    # 6. 26845416039893360305516015851501077574841          = 154456071032310651803 × 173806156407264626747
    # 7. 2146776870009792253322117406137065611833216495831      = 1189877692142508366049463 × 1804199611595608193523937
    rozloz_prvo = [ [1, 1], [1, 1], [1, 1], [1065807076247, 1245640800979], [16548342710737441, 19935364988729123],
                   [154456071032310651803, 173806156407264626747], [1189877692142508366049463, 1804199611595608193523937] ]

    index_uloh= 2 # zadaj index pre vykonanie ulohy N # : index_uloh = N

    if index_uloh -1 < len(prvo_cis) and index_uloh > 0:

        n = prvo_cis[index_uloh-1] # 2146776870009792253322117406137065611833216495831
        if index_uloh < 3 : # pre 1. 2.
            start_cas = time.time()
            vrat = factorize_via_6k(n)  # factorize(n) # factorize_via_sqrt(n)
            end_cas = time.time()
            print(f"Cas vykonavania factorize_via_6k(n): {end_cas - start_cas} secund\n")

        elif index_uloh == 3:  # 3. prvocislo
            start_cas = time.time()
            vrat = factorize_via_6k_long_numbers(n) #
            end_cas = time.time()
            print(f"Cas vykonavania factorize_via_6k(n): {end_cas - start_cas} secund\n")
        else:
            vrat= rozloz_prvo[index_uloh-1][:] 
            print(f"Rozklad modulu n = { n } na prvocinitele: {vrat}\n")
        p = vrat[0] #101279
        q = vrat[1]#1637177#130027
        n = p * q
        print(f"n: {n }\n")
        fi_n = (p-1)*(q-1) # vypocet fi_n, sluzi ako module pre vypocet d: sokromni kluc
        print(f"Fi_n: {fi_n}\n")
        e = 65537  
        d = modInverse(e, fi_n)
        print(f"d: {d} inverzne k e\n")
        # zasifrovana sprava:
        # 1. 1325266873785 # 2. 1990249581724467 # 3. 147885702766350471578
        # 4. 1075593273482743198269527   # 5. 22712629296843271867140518185260
        # 6. 6820997247850432766042868007364587250604
        # 7. 604615692674313046352476676786807225671015935385
        sifrov_spr = [ 1325266873785, 1990249581724467, 147885702766350471578,  1075593273482743198269527, 22712629296843271867140518185260,
                          6820997247850432766042868007364587250604, 604615692674313046352476676786807225671015935385 ]
        y = sifrov_spr[index_uloh-1]
        x = pow(y, d, n)
        print(f"x: {x} desifrovana sprava\n")
    else:
        print(f"Hodonta {index_uloh} je mimo limit {len(prvo_cis)}, moze byt <1, 7>\n")
     # sprava je vzdi:  1234567890