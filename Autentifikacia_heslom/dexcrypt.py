import base64

def extract_and_convert_hashes(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    login_hash_salt_triples = []
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 3:
            login, salt, hash_b64 = parts  
            try:
                hash_bytes = base64.b64decode(hash_b64)
                hash_hex = hash_bytes.hex()
                login_hash_salt_triples.append(f"{login}:{hash_hex}:{salt}")  
            except Exception as e:
                print(f"Error decoding base64: {e}")
                continue  

    with open(output_file_path, 'w', encoding='utf-8') as new_file:
        for triple in login_hash_salt_triples:
            new_file.write(triple + '\n')

                  
input_file_path = "./Autentifikacia_heslom/shadow1.txt"
output_file_path = "./Autentifikacia_heslom/login_hash.txt"
extract_and_convert_hashes(input_file_path, output_file_path)


#hashcat -m 10 -a 3 --username -o cracked_passwords.txt shadow1.txt  -1?l?u?d ?1?1?1?1?1 --increment --increment-min 4 
"""
shadow1
c81b9ec61ba2b8ec562fa40d4f663b90:83muHdsn:ZH0n
c5a216b3777cd5bc0e72289048f2d600:1mRCTqle:e1VL
03be23a5084048e50290b26b898f243d:SLmX5Uua:s7xG
2de6cbbea44a8afc86c724defd22c973:3B0hFRav:katkA
33548f2307cb1099a92b87a2ae262677:ZTXfkOqQ:petkO

shadow2
8c2970b26f2b5767231618a11c0216e6:Wp4yHin9:D0C1
84817d5d6f9adcb2ff6efc780dbb0667:DuMbRYmy:ZH0n
6bb3768acdd4b4e769fb5a1dab9d6357:ZPSCovmD:Cl3I

shadow3
8c2970b26f2b5767231618a11c0216e6:Wp4yHin9:D0C1
84817d5d6f9adcb2ff6efc780dbb0667:DuMbRYmy:ZH0n
6bb3768acdd4b4e769fb5a1dab9d6357:ZPSCovmD:Cl3I
f14082789ab08234abd86131d1f60eb5:XbmPIzdV:ZH0n
9f29691faa483b5878fac8f79ec95d14:t6RFkrjT:ow2K
5a08476929931202da4c104749777ab0:MykpFFEW:0y1W
e2b06c283afc7e863dd9e00e127d289b:Iwjsc2Tb:petkO

shadow4
8c2970b26f2b5767231618a11c0216e6:Wp4yHin9:D0C1
84817d5d6f9adcb2ff6efc780dbb0667:DuMbRYmy:ZH0n
6bb3768acdd4b4e769fb5a1dab9d6357:ZPSCovmD:Cl3I
f14082789ab08234abd86131d1f60eb5:XbmPIzdV:ZH0n
9f29691faa483b5878fac8f79ec95d14:t6RFkrjT:ow2K
5a08476929931202da4c104749777ab0:MykpFFEW:0y1W
e2b06c283afc7e863dd9e00e127d289b:Iwjsc2Tb:petkO
570a49413df1a7f0a9b1a1851c412989:3i6bbjaT:e1VL
6c38bb95e77b5f3280cbc1296e1fe76b:laTf36nF:0y1W
e2a0ec78f0a1333251633c4185a22475:PlbP2r3V:9YyU
1829ef19d0f06549c67d8345ab0e0b94:lwDTZIfw:leNka
"""





