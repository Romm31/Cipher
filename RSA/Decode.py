from Crypto.Util.number import long_to_bytes, inverse

def rsa_decode_plaintext_only(c, e, n, p, q):
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    try:
        return long_to_bytes(m).decode()
    except:
        return '[Bukan UTF-8 valid]'

# === INPUT MANUAL ===
c = int(input("Masukkan nilai Ciphertext (C): "))
e = int(input("Masukkan nilai E: "))
n = int(input("Masukkan nilai N: "))
p = int(input("Masukkan nilai P: "))
q = int(input("Masukkan nilai Q: "))

# Dekripsi dan output langsung hasilnya
plaintext = rsa_decode_plaintext_only(c, e, n, p, q)

print("\n=== HASIL DECODE ===")
print(f"{plaintext}")