import base64

def reencode_hashes_to_base64(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                hash_hex, password = parts
                hash_bytes = bytes.fromhex(hash_hex)
                hash_base64 = base64.b64encode(hash_bytes).decode('utf-8')
                out_file.write(f"{hash_base64}:{password}\n")

# Specify your actual file paths here
input_file_path = 'D:\\projekty\\VScode\\Autentifikacia_heslom\\hashes2.txt'
output_file_path = 'D:\\projekty\\VScode\\Autentifikacia_heslom\\output.txt'

# Call the function with the actual paths
reencode_hashes_to_base64(input_file_path, output_file_path)