import base64

def extract_and_convert_hashes(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    login_hash_pairs = []
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 3:
            login, _, hash_b64 = parts  # Zmena tu: ignorujeme soľ
            try:
                hash_bytes = base64.b64decode(hash_b64)
                hash_hex = hash_bytes.hex()
                login_hash_pairs.append(f"{login}:{hash_hex}")  # Zmena tu: pridávame len login a hash
            except Exception as e:
                print(f"Error decoding base64: {e}")
                continue  # If an error occurs during decoding, skip this line

    with open(output_file_path, 'w', encoding='utf-8') as new_file:
        for pair in login_hash_pairs:
            new_file.write(pair + '\n')

# Replace these paths with the actual paths on your system
input_file_path = 'D:\\projekty\\VScode\\Autentifikacia_heslom\\shadow1.txt'
output_file_path = 'D:\\projekty\\VScode\\Autentifikacia_heslom\\login_hash.txt'

# Call the function with the file paths
extract_and_convert_hashes(input_file_path, output_file_path)
