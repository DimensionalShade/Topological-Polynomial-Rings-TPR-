import plotext as plt

def visualize(ciphertext, modulus):
    coeffs = [ord(c) % modulus for c in ciphertext]
    support = [i for i, c in enumerate(coeffs) if c != 0]
    plt.plot(support, coeffs)
    plt.title("TPR Support Visualization")
    plt.show()

if __name__ == "__main__":
    ciphertext = "TPR{g3n3r1c_3ncrypt10n}"
    modulus = 17
    visualize(ciphertext, modulus)
