from discrete import DiscreteRandomVariable, ConstantRandomVariable
from numpy import prod
from math import sqrt

class U(DiscreteRandomVariable):
    def __init__(self, n, i):
        weights = {j : 1 for j in range(n)}
        super().__init__(weights)

class C(DiscreteRandomVariable):
    def __init__(self, n):
        weights = {i : prod([1 - j / n for j in range(1, i - 1)]) - prod([1 - j / n for j in range(1, i)]) for i in range(2, n + 2)}
        super().__init__(weights)

class Z(DiscreteRandomVariable):
    def __init__(self, n):
        super().__init__(((C(n) - ConstantRandomVariable(1)) / ConstantRandomVariable(sqrt(n))).pmf())

if __name__ == '__main__':
    # the probability that 2 persons have distinct birthdays in a year of 365 days
    print(1 - C(365).cdf(2))
    # the probability that 23 persons have distinct birthdays in a year of 365 days
    print(1 - C(365).cdf(23))
    # the probability that 366 persons have distinct birthdays in a year of 365 days
    print(1 - C(365).cdf(366))