import base64

def encode_base64(data):
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(encoded_data):
    try:
        decoded_bytes = base64.b64decode(encoded_data)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error decoding Base64: {e}"

def encode_base32(data):
    encoded_bytes = base64.b32encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base32(encoded_data):
    try:
        decoded_bytes = base64.b32decode(encoded_data)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error decoding Base32: {e}"

def main():
    print("Pilih metode:")
    print("1. Encode Base64")
    print("2. Decode Base64")
    print("3. Encode Base32")
    print("4. Decode Base32")
    
    choice = input("Masukkan pilihan (1/2/3/4): ")
    
    if choice == '1':
        data = input("Masukkan string yang ingin di-encode ke Base64: ")
        encoded_result = encode_base64(data)
        print(f'Hasil encode Base64: {encoded_result}')
    elif choice == '2':
        encoded_data = input("Masukkan string Base64 yang ingin di-decode: ")
        decoded_result = decode_base64(encoded_data)
        print(f'Hasil decode Base64: {decoded_result}')
    elif choice == '3':
        data = input("Masukkan string yang ingin di-encode ke Base32: ")
        encoded_result = encode_base32(data)
        print(f'Hasil encode Base32: {encoded_result}')
    elif choice == '4':
        encoded_data = input("Masukkan string Base32 yang ingin di-decode: ")
        decoded_result = decode_base32(encoded_data)
        print(f'Hasil decode Base32: {decoded_result}')
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
