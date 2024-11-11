# Frekvencna analyza v jazyku bez medzier
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
## -------------------- Sifrovanie a desifrovnaie -----------------------------------------------------------
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
    print("\nText from decrypting: %s" %plain_t)
    return plain_t
## -------------------- Koniec Sifrovanie a desifrovnaie -----------------------------------------------------------

## -------------------- Spracovanie textu ------------------------------------------------------------------------
# funkcia: citanie zo suboru
def read_file( filename ):
    f= open( filename )
    text = f.read()
    return text
# funkcia: nahradi medzeru prezdnim znakom
def clear_space( text ):
    clr_t = text.replace(" ", "")
    return clr_t
## -------------------- Koniec Spracovanie textu ------------------------------------------------------------------------

## -------------------- Odhada dlzky hesla --------------------------------------------------------------
# funkcia: hlada v texte n rovnakych znakov(napr. trojice), vrati vzdialenost medzi ich vyskitom 
# -trojic napr. 0, 700; 700; RIA RIA [pozicia. 1., pozicia. 2.; vzdialenost; n-tica znakov 1., n-tica znakov 2.]
def kasiski( text, n ):
    distance = []
    for i in range(0, len(text) -n -1):
        for j in range(i+1, len(text) -n):
            t1 = text[i:i+n]
            t2 = text[j:j+n]
            if (t1 == t2):
                # vypise: napr. 0 700 700 RIA RIA [pozicia. 1., pozicia. 2.; vzdialenost; n-tica znakov 1., n-tica znakov 2.]
                print(i, j, j - i, t1, t2)
                distance.append(j - i)
    return distance

# funkcia: vola funkciu kasiski s defaultne trojicami rovnakych znakov, vrati delitele vzdialenosti a ich pocetnost
# -1. kontr. vypis textu bez medzier, 2. vypis vzdialenosti medzi n-ticami (tojicami)
# -3. vypis delitelov a pocet vzdialenosti ktore su nim delitelne. 
def find_coutn_of( text, n= 3):
    clr_text = clear_space( text )
    # kontrolny vypis textu bez medzier
    print(clr_text)
    dist_tex = kasiski(clr_text, n)
    dist_tex.sort()
    # 2. vypisuje v poradi vzdialenosti medzi n-ticami (Trojicami) znakov 
    # [2, 25, 25, ..., 225, 225, 225, 225,  660, 700, 713]
    print(dist_tex)

    # 3.
    mux_n = range(2,42)#[4, 5, 6, 7, 8, 9, 10] # 2, 3,
    num_of = [0] * len(mux_n)
    for i in range(len(dist_tex)):
        for m_i in range(len(mux_n)):
            if dist_tex[i] % mux_n[m_i] == 0:
                num_of[m_i] = num_of[m_i] + 1

    for ix in range(len(num_of)):
        # vypise delitel /mux_n[ix]/ a pocet vzdialenosti /num_of[ix]/ ktore boli delitelne
        print(mux_n[ix], ": ", num_of[ix])
    return num_of
## ------------------- Koniec Odhada dlzky hesla -------------------------------------------------------

## ------------------- Hladanie znakov hesla -----------------------------------------------------------
# funkcia: vypocita odhad index koincidencie
def index_coincidence( f_text ):

    multiplicities = [ f_text.count(c_a) for c_a in alphab_a]
    total = sum(multiplicities)
    ind_coinc = 0.
    for m in multiplicities:
        #print("%2d : %6.4f" % (i, prav_Zn[i]))
        ind_coinc += (float(m)/ float(total)) * (float(m-1) / float(total -1))
    #print("index koincindenicie: %6.4f pravdepodobost znaku %6.4f" % (ind_koinc, prv_Ze))
    return ind_coinc

# funkcia: rozdeli text /in_text/ podla poctu /key_l/ znakov v hesle 
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

# funkcia: vypocita pravdepodobnost vyskitu znaku v texte /massage/, vrati pole pravdepodobnosti pismena A az Z
# --frekvencna analyza textu 
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
# funkcia: vrati vydialenost medzi prevdepodobnostami, Rozdielom 
# --index koincidencie
def get_distance( prob1, prob2):
    # podal: sum( p(a_i)^2) -> pre i =1 az q (max pismeno)
    dist_prob= [  (prob1[i] - prob2[i])**2 for i in  range(0, len(prob1))]
    return sum(dist_prob)
# funkcia: posunie text o znak do lava
def rotate_left(array):
    tmp = array[0]
    for i in range(0, len(array) -1):
        array[i] = array[i+1]
    array[len(array) -1] = tmp
    return array

# funkcia: po zadani prepokladanej dlyky hesla key_len, vypise heslo a vrati desifrovany text
# -/eng_enab/ defaultne /True/, je priznak ci ma porovnavat sifrovani text s pravdepodobnostou vyskitu v Ang alebo v Slov
# -1. vymaze medzeru z textu;       2. rozdeli sifrovany text na riadky o dhlzke /key_len/ znakou 
# -3. vypis pre kontrolu spravnej jazykovej frekve. analyzi; 
# -4. Ukazka (vypisom) hladania 1. znaku hesla (znak s najmensim cislom)
# -5. realne hlada znaky hesla cez posuvanie o znak; 6. konrolne desifrovnie textu heslom
def find_key( in_text, key_len, eng_enab):
    clr_text = clear_space(in_text)
    if eng_enab:
        frekv_uni_prob = frekv_prob
    else: 
        frekv_uni_prob = frekv_slov_prob

    #2.
    cesar_strings = []
    # rozdeli text na n riadkov o dlzke (stlpcoch) /key_len/
    #   v podstaten jeden stlpec je len posunutie ako v pripade Cezarovej sifri
    cesar_strings = split_text(clr_text, key_len)
    # prevdepodobnost znakov v texte; frekvencan analyza sifrovaneho textu
    massag_prob = get_probabilities(clr_text)

    # kontrolny vypis frekvencna analyza textu v jazyku SK/ENG /frekv_uni_prob/, a frekvencna analyza sifrovaneho textu /massag_prob/
    # napr.  A	0.0995	0.0529 \n  B	0.0118	0.0290  ....
    print_probabilities(frekv_uni_prob, massag_prob)
    distanc_of_prob = get_distance(frekv_uni_prob, massag_prob)
    # index koincidencie textu -----------------------------

    # 3. kotrola spravnej jazykovej frekven. analyzi
    probabilities = get_probabilities(cesar_strings[0])
    # index koincidencie pre znaky sifrovene 1. znakom hesal /cesar_strings[0]/
    # index koincidencie je pravdepodobnost priblizne rovna pravdepodobnosti vyskitu 1/n znakov P= (1/26) ~ 0,03846153846
    # ak je pouzita sprvna jazykova analzyza 

    # vypis indexu koincidencie pre 1. znak helsa, sluzi na porovanie ci sa jedna o rovnomerne rodelenie
    # ak je cislo blizke P= (1/26) ~ 0,03846153846, je pouzita spravna jazykova frekvencna analyza (SK / ENG)
    print("index koenc. = " + str(get_distance(frekv_uni_prob, probabilities)))

    # 4. hlada znaky hesla -------------------------------------
    # test a vypis pre pouyivatela
    if eng_enab:
        print("distance betwen prob of ENG and encr. text")
    else: 
        print("distance betwen prob of SK and encr. text")
    for i in range(0, len(alphab_a)):
        # vypis znaku a indexu koincidencie 
        print("%c\t%.5f" % (alphab_a[i], (get_distance(frekv_uni_prob, probabilities))))
        rotate_left(probabilities)
    
    # 5. realne hlada znaky hesla
    # heslo /str_k/  
    str_k = ""
    #cesar_string = cesar_char 
    for cesar_string in cesar_strings:
        # pre n-ty znak z riadkou vypocita provdepodobnost, napr. 2. znak v kazdom riadku (o dlzke hesla) zasifrovaneho textu
        probabilities = get_probabilities(cesar_string)
        possibilities = []
        for i in range(0, len(alphab_a)):
            # ulozi do /tuple/ Rozdiel pravdepodobnoti frek. jazika a sifrovaneho textu, Znak ako ASCII hodnotu
            tuple = (get_distance(frekv_uni_prob, probabilities), (alphab_a[i]))
            possibilities.append(tuple)
            rotate_left(probabilities)
        # vypis znaku helsa po riakoch
        print(min(possibilities)[1])
        # ked najde minimum ulozi honodtu ASCII ako potencialny znak hesla
        str_k += min(possibilities)[1]
    # vypis celeho hesla po ako slovo
    print(str_k)  

    # 6. konrolne desifrovnie textu heslom
    plain_text= viegenere_decrypt(in_text, str_k)
    return plain_text, str_k
## ------------------- Koniec Hladanie znakov hesla -----------------------------------------------------------------


def main():
    file_text = ""
    file_text = read_file("./ViegenerovskaSIfra/uc1_krypto_2022_u1_text2_enc.txt")

    # /key_try/: pouzivatel nastavi podal totho co vypise funkcia: /find_count_of(file_text)/; default: 0
    key_try = 0
    # /heslo/: pouzivatel nastavi ak potrebuje doladit znaky hesla; default: ""
    heslo = "" 
    enc_now_text = ""

    if key_try == 0 and heslo == "":
        find_coutn_of(file_text)
    
    if key_try != 0 and heslo == "":
        enc_now_text, heslo = find_key(file_text, key_try, False)
    elif heslo != "":
        key_try = len(heslo)
        print("Added by user heslo: {}, len of (key_try): {}\n".format(heslo, key_try))
        enc_now_text = viegenere_decrypt(file_text, heslo)
        

    # vypise prvu 1/5 textu na kontrolou spravnosti desifrovania, podla dlzky hesla, pozor aj s medzermi
    print("\nTESTIKY\n") 
    if enc_now_text != "":
        for i in range(0, len(enc_now_text) // 5, key_try):
            print("Test %s\n" % enc_now_text[i:(key_try + i)])
# --------------------- tu sa zacina vykonavat program ---------------------------------------
main()
   # key of text1 QWERTYUIOPASDFG lenght_of_key 15 sk
   # key of text2 AUZDMZRNFUXQSXHORWQLCLZLS lenght_of_key 25 sk
   # key of text3 LIYZKFOREGYSDTRQNTK  lenght_of_key 19 sk
   # key of text4 IDGKZQNOMYNTJOUIB  lenght_of_key 17 en
   # length of key <15, 25>