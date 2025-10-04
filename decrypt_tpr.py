def decrypt_tpr(ciphertext, modulus):
    coeffs = [ord(c) % modulus for c in ciphertext]
    support = [i for i, c in enumerate(coeffs) if c != 0]
    tags = {i: f"char:{ciphertext[i]}" for i in support}
    return support, tags

def audit(support, tags):
    print("TPR Decryption Audit:")
    for i in support:
        print(f"  ▓ index {i} → {tags[i]}")
    print(f"\nTotal support: {len(support)}")

if __name__ == "__main__":
    ciphertext = "TPR{g3n3r1c_3ncrypt10n}"
    modulus = 17
    support, tags = decrypt_tpr(ciphertext, modulus)
    audit(support, tags)
