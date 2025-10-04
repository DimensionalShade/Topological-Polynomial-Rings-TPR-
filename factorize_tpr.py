def factorize_tpr(N):
    coeffs = [1 if N % i == 0 else 0 for i in range(2, N)]
    support = [i for i, c in enumerate(coeffs, start=2) if c != 0]
    tags = {i: 'prime' if is_prime(i) else 'composite' for i in support}
    return support, tags

def is_prime(n):
    return all(n % d != 0 for d in range(2, int(n**0.5)+1))

def audit(support, tags):
    print("TPR Factorization Audit:")
    for i in support:
        print(f"  ▓ {i} → {tags[i]}")
    print(f"\nTotal support: {len(support)}")
    print(f"Primes: {[i for i in support if tags[i] == 'prime']}")
    print(f"Composites: {[i for i in support if tags[i] == 'composite']}")

if __name__ == "__main__":
    N = 105
    support, tags = factorize_tpr(N)
    audit(support, tags)
