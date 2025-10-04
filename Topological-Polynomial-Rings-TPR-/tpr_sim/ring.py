class PolynomialRing:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # list of a_i

    def __str__(self):
        return ' + '.join(f'{a}x^{i}' for i, a in enumerate(self.coefficients) if a != 0)

    def add(self, other):
        length = max(len(self.coefficients), len(other.coefficients))
        result = [0] * length
        for i in range(length):
            a = self.coefficients[i] if i < len(self.coefficients) else 0
            b = other.coefficients[i] if i < len(other.coefficients) else 0
            result[i] = a + b
        return PolynomialRing(result)
