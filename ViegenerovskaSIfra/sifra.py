# pravdepodobost vyskitu znakov v Ang
frekv_prob =    [ 0.0657, 0.0126, 0.0399, 0.0322, 0.0957, 0.0175, 0.0145, 0.0404, 0.0701, 0.0012, 0.0049,
                   0.0246, 0.0231, 0.0551, 0.0603, 0.0298, 0.0005, 0.0576, 0.0581, 0.0842, 0.0192, 0.0081,
                   0.0086, 0.0007, 0.0167, 0.0005]
# pravdepodobnost vyskitu znakov v Slov
frekv_slov_prob = [ 0.0995, 0.0118, 0.0266, 0.0436, 0.0698, 0.0113, 0.0017, 0.0175, 0.0711, 0.0157, 0.0406,
                    0.0262, 0.0354, 0.0646, 0.0812, 0.0179, 0.0000, 0.0428, 0.0463, 0.0432, 0.0384, 0.0314,
                    0.0000, 0.0004, 0.0170, 0.0175]
# do alphab_b sa ulozi abeceda
alphab_a = []
for i in range(len(frekv_prob)):
    alphab_a += chr(i+ 65) #
# funkcia: zasifrovanie textu viegenerovou sifrou, vrati sifrovany text
def viegenere_encrypt(plain_t, key):
    cipher_t = ""
    key_pos = 0
    for c_ch in plain_t:
        if c_ch >= 'A' and c_ch <= 'Z':
            cipher_t = cipher_t + chr((ord(c_ch) +  ord(key[key_pos])) % 26 + ord("A"))
            key_pos = key_pos + 1
            if key_pos >= len(key):
                key_pos = 0
        else:
            cipher_t += c_ch
    return cipher_t
# funkcia: desifrovanie textu viegenerovou sifrou, vrati desifrovany text
def viegenere_decrypt( cipher_t, key):
    plain_t = ""
    key_pos =0
    print(" key: %s\n cipher : %s" %(key, cipher_t))
    for c_ch in cipher_t:
        if c_ch >= 'A' and c_ch <= 'Z':
            plain_t = plain_t + chr( ( ord(c_ch) +26 - ord(key[key_pos]) ) %26 + ord("A"))
            key_pos= key_pos + 1
            if key_pos >= len(key):
                key_pos = 0
        else:
            plain_t+= c_ch
    print("Text from decrypting: %s" %plain_t)
    return plain_t
# funkcia: citanie zo suboru
def read_file( filename ):
    f= open( filename )
    text = f.read()
    return text
# funkcia: nahradi medyeru prezdnim znakom
def clear_space( text ):
    clr_t = text.replace(" ", "")
    return clr_t
# funkcia: hlada v texte n rovnakych znakov, vrati vzdialenost medzi ich vyskitom
def kasiski( text, n ):
    distance = []
    for i in range(0, len(text) -n -1):
        for j in range(i+1, len(text) -n):
            t1 = text[i:i+n]
            t2 = text[j:j+n]
            if (t1 == t2):
                print(i, j, j - i, t1, t2)
                distance.append(j - i)
    return distance
# funkcia: vola funkciu kasiski s defaltne trojicami rovnakych znakov, vrati delitele vydialenosti a ich pocetnost
def find_coutn_of( text, n= 3):
    clr_text = clear_space( text )
    print(clr_text)
    dist_tex = kasiski(clr_text, n)
    dist_tex.sort()
    print(dist_tex)

    mux_n = range(2,30)#[4, 5, 6, 7, 8, 9, 10] # 2, 3,
    num_of = [0] * len(mux_n)
    for i in range(len(dist_tex)):
        for m_i in range(len(mux_n)):
            if dist_tex[i] % mux_n[m_i] == 0:
                num_of[m_i] = num_of[m_i] + 1

    for ix in range(len(num_of)):
        print(mux_n[ix], ": ", num_of[ix])
    return num_of

# funkcia: vypocita index koincidencie
def index_coincidence( f_text ):

    multiplicities = [ f_text.count(c_a) for c_a in alphab_a]
    total = sum(multiplicities)
    ind_coinc = 0.
    for m in multiplicities:
        #print("%2d : %6.4f" % (i, prav_Zn[i]))
        ind_coinc += (float(m)/ float(total)) * (float(m-1) / float(total -1))
    #print("index koincindenicie: %6.4f pravdepodobost znaku %6.4f" % (ind_koinc, prv_Ze))
    return ind_coinc

# funkcia: rozdeli text podla poctu znakov v hesle key_l
def split_text(in_text, key_l):
    #print(in_text)
    edited_text = clear_space(in_text)
    #print(edited_text)
    string_row = []
    for ind_c in range(0, key_l):
        string_row.append("".join(edited_text[ind_c_r] for ind_c_r in range(ind_c, len(edited_text), key_l)))
    #print(string_row)
    return string_row
# funkcia: spocita vyskit znaku v texte
def count_Chars(massage):
    msg = massage.upper()
    multiplicities = [ msg.count(i) for i in alphab_a ] #alphabet
    return multiplicities

# funkcia: vypocita pravdepodobnost vyskitu znaku v texte massage
def get_probabilities( massage):
    multiplicities= count_Chars(massage)
    total = sum(multiplicities)
    probabilities= [ float(n) / float(total) for n in multiplicities ]
    return probabilities
# funkcia: vypise znaky a ich pravdepodobnost
def print_probabilities(probabilities):
    for i in range(0, len(alphab_a)):
        print("%c\t%.4" % (alphab_a[i],probabilities[i] ))
# funkcia: vypise znaky a dve pravdepodobnost, pre porovnaie
def print_probabilities(prob1, prob2):
    for i in range(0, len(alphab_a)):
        print("%c\t%.4f\t%.4f " %(alphab_a[i], prob1[i], prob2[i]))
# funkcia: vrati vydialenost medzi prevdepodobnostami
def get_distance( prob1, prob2):
    dist_prob= [  (prob1[i] - prob2[i])**2 for i in  range(0, len(prob1))]
    return sum(dist_prob)
# funkcia: podunie text o znak do lava
def rotate_left(array):
    tmp = array[0]
    for i in range(0, len(array) -1):
        array[i] = array[i+1]
    array[len(array) -1] = tmp
    return array
# funkcia: po zadani prepokladanej dlyky hesla key_len, vypise heslo a vrati desifrovany text
# eng_enab defaltne True, je priznak ci ma porovnavat sifrovani text s pravdepodobnostou vyskitu v Ang alebo v Slov
def find_key( in_text, key_len, eng_enab= True):
    clr_text = clear_space(in_text)
    if eng_enab == True:
        frekv_uni_prob = frekv_prob
    else: frekv_uni_prob = frekv_slov_prob
    cesar_strings = []
    cesar_strings = split_text(clr_text, key_len)
    massag_prob = get_probabilities(clr_text)


    print_probabilities(frekv_uni_prob, massag_prob)
    distanc_of_prob = get_distance(frekv_uni_prob, massag_prob)
    print(distanc_of_prob)
    from math import sqrt
    print(sqrt(distanc_of_prob)) #Zoberiem všetky znaky, ktoré boli zaheslované prvým znakom hesla get_probabilities(cesar_strings[0])
    probabilities = get_probabilities(cesar_strings[0])
    print(get_distance(frekv_uni_prob, probabilities)) # keď táto pravdepodobnosť sa blíži pravdepodobnosti výskytu v rovnomernom rozdelení, p ~ 1/26, alebo 1/n ak by bolo viac znakov

    print("distance betwen prob of eng and encr text")
    for i in range(0, len(alphab_a)):
        print("%c\t%.5f" % (alphab_a[i], (get_distance(frekv_uni_prob, probabilities))))
        rotate_left(probabilities)
    str_k = ""
    for cesar_string in cesar_strings:
        probabilities = get_probabilities(cesar_string)
        possibilities = []
        for i in range(0, len(alphab_a)):
            tuple = (get_distance(frekv_uni_prob, probabilities), (alphab_a[i]))
            possibilities.append(tuple)
            rotate_left(probabilities)
        print(min(possibilities)[1])
        str_k += min(possibilities)[1]
    print(str_k)  # "QWERTYUEOPASDFG"

    plain_text= viegenere_decrypt(file_text, str_k)
    print(plain_text) # viegenere_encrypt(plain_text, str_k)
    return plain_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_text = read_file("./uc1_krypto_2022_u1_text2_enc.txt")

    find_coutn_of( file_text)
    # po najdeni spravej dlzky hesla treba prepisat key_try
    key_try=25

    enc_now_text = ""
    if key_try != 0:     
        enc_now_text= find_key( file_text, key_try, eng_enab= False)
    # vypise prvu 1/5 textu na kontrlou spravnosti desifrovania, podla dlykz hesla
    if enc_now_text != "":
        for i in range(0,len(enc_now_text)//5, key_try):
            print("Test %s\n" %enc_now_text[i:(key_try+i)])
    # poznamky:
    # key of text1 QWERTYUIOPASDFG long 15 ok in slov
    # key of text2 AUZDMZRNFUXQSXHORWQLCLZLS long 25 ok in slov