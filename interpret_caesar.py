def caesar_encrypt(text, shift):
    return ''.join(chr((ord(c) - 32 + shift) % 95 + 32) for c in text)

def interpret_caesar(ciphertext, modulus):
    coeffs = [ord(c) % modulus for c in ciphertext]
    support = [i for i, c in enumerate(coeffs) if c != 0]
    tags = {i: f"char:{ciphertext[i]}" for i in support}
    return support, tags

def audit(support, tags):
    print("TPR Caesar Interpretation Audit:")
    for i in support:
        print(f"  ▓ index {i} → {tags[i]}")
    print(f"\nTotal support: {len(support)}")

if __name__ == "__main__":
    plaintext = "TPR_interprets_structure"
    shift = 7
    modulus = 17
    ciphertext = caesar_encrypt(plaintext, shift)
    support, tags = interpret_caesar(ciphertext, modulus)
    audit(support, tags)
