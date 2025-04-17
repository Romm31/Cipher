def caesar_encode(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - offset + key) % 26 + offset)
            result += encoded_char
        else:
            result += char
    return result

def caesar_bruteforce(ciphertext):
    print("\n brute-force Caesar Cipher:")
    for shift in range(1, 26):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                offset = ord('A') if char.isupper() else ord('a')
                decoded_char = chr((ord(char) - offset - shift) % 26 + offset)
                result += decoded_char
            else:
                result += char
        print(f"[Shift {shift:2}] {result}")

# Input
mode = input("Ketik salah satu(encode/decode): ").strip().lower()

if mode == "encode":
    plaintext = input("Masukkan plaintext: ")
    key = int(input("Masukkan key (0-25): "))
    encoded = caesar_encode(plaintext, key)
    print("\n🔐 Hasil Caesar Cipher (encoded):")
    print(encoded)

elif mode == "decode":
    ciphertext = input("Masukkan ciphertext: ")
    caesar_bruteforce(ciphertext)

else:
    print("Bukan Caesar Cipher!")
