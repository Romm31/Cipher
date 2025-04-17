def string_to_hex(s):
    """Convert a string to hexadecimal."""
    return s.encode('utf-8').hex()

def hex_to_string(h):
    """Convert hexadecimal to a string."""
    bytes_object = bytes.fromhex(h)
    return bytes_object.decode('utf-8', errors='ignore')

def vigenere_encode(plaintext, key):
    """Encode plaintext using Vigenère cipher."""
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    encoded = []
    for p, k in zip(plaintext, key):
        encoded_char = chr((ord(p) + ord(k)) % 256)
        encoded.append(encoded_char)
    return ''.join(encoded)

def vigenere_decode(ciphertext, key):
    """Decode ciphertext using Vigenère cipher."""
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decoded = []
    for c, k in zip(ciphertext, key):
        decoded_char = chr((ord(c) - ord(k)) % 256)
        decoded.append(decoded_char)
    return ''.join(decoded)

def main():
    print("Pilih metode:")
    print("1. String to Hex")
    print("2. Hex to String")
    print("3. Vigenère Encode")
    print("4. Vigenère Decode")
    
    choice = input("Masukkan pilihan (1/2/3/4): ")
    
    if choice == '1':
        data = input("Masukkan string yang ingin diubah ke Hex: ")
        hex_result = string_to_hex(data)
        print(f'Hasil Hex: {hex_result}')
    elif choice == '2':
        hex_data = input("Masukkan string Hex yang ingin diubah ke String: ")
        string_result = hex_to_string(hex_data)
        print(f'Hasil String: {string_result}')
    elif choice == '3':
        plaintext = input("Masukkan plaintext yang ingin di-encode: ")
        key = input("Masukkan kunci Vigenère: ")
        encoded_result = vigenere_encode(plaintext, key)
        print(f'Hasil Vigenère Encode: {encoded_result}')
    elif choice == '4':
        ciphertext = input("Masukkan ciphertext yang ingin di-decode: ")
        key = input("Masukkan kunci Vigenère: ")
        decoded_result = vigenere_decode(ciphertext, key)
        print(f'Hasil Vigenère Decode: {decoded_result}')
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
