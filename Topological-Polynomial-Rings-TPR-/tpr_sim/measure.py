class PolynomialMeasure:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def norm(self):
        # Sum of absolute values as a simple norm
        return sum(abs(a) for a in self.coefficients)

    def fixate(self):
        # Freeze as immutable artifact
        return tuple(self.coefficients)

    def cli_repr(self):
        # CLI-friendly output
        return ' + '.join(f'{a}x^{i}' for i, a in enumerate(self.coefficients) if a != 0)
