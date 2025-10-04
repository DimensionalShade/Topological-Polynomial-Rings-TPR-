def tpr_lang(text, modulus):
    coeffs = [ord(c) % modulus for c in text]
    support = [i for i, c in enumerate(coeffs) if c != 0]
    tags = {i: f"symbol:{text[i]}" for i in support}
    meaning = f"TPR sees {len(support)} resonant points in '{text}'"
    return support, tags, meaning

def audit(support, tags, meaning):
    print("TPR Language Audit:")
    for i in support:
        print(f"  ▓ index {i} → {tags[i]}")
    print(f"\n{meaning}")

if __name__ == "__main__":
    text = "TPR is not an algorithm. It is a lens."
    modulus = 17
    support, tags, meaning = tpr_lang(text, modulus)
    audit(support, tags, meaning)
