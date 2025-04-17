from Crypto.Util.number import bytes_to_long, inverse, getPrime
import random

def generate_rsa_keys(bits=512):
    e = 65537
    while True:
        p = getPrime(bits)
        q = getPrime(bits)
        if p != q:
            phi = (p - 1) * (q - 1)
            if phi % e != 0:
                try:
                    d = inverse(e, phi)
                    break
                except ValueError:
                    continue
    n = p * q
    return e, d, n, p, q

def rsa_encode_auto(plaintext):
    e, d, n, p, q = generate_rsa_keys()
    m = bytes_to_long(plaintext.encode())
    c = pow(m, e, n)
    
    return {
        "Plaintext": plaintext,
        "Plaintext (int)": m,
        "Ciphertext (C)": c,
        "Public Key (E)": e,
        "Private Key (D)": d,
        "Modulus (N)": n,
        "P": p,
        "Q": q
    }

# === INPUT MANUAL ===
plaintext = input("Masukkan plaintext: ")

# Proses enkripsi otomatis
hasil = rsa_encode_auto(plaintext)

print("\n=== HASIL ENKRIPSI (RSA Otomatis) ===")
for k, v in hasil.items():
    print(f"{k}: {v}")
