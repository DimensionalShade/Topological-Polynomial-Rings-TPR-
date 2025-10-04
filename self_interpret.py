def tpr_self(path, modulus):
    with open(path) as f:
        text = f.read()
    coeffs = [ord(c) % modulus for c in text]
    support = [i for i, c in enumerate(coeffs) if c != 0]
    tags = {i: f"char:{text[i]}" for i in support}
    meaning = f"TPR sees {len(support)} resonant points in its own structure"
    return support, tags, meaning

def audit(support, tags, meaning):
    print("TPR Self-Interpretation:")
    for i in support[:20]:
        print(f"  ▓ index {i} → {tags[i]}")
    print(f"\n{meaning}")

if __name__ == "__main__":
    path = "TPR.md"
    modulus = 17
    support, tags, meaning = tpr_self(path, modulus)
    audit(support, tags, meaning)
