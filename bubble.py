from discrete import DiscreteRandomVariable, ConstantRandomVariable
from numpy import prod
from math import sqrt

class V(DiscreteRandomVariable):
    def __init__(self, n, i):
        weights = {j : 1 for j in range(n - i + 1)}
        super().__init__(weights)

class P(DiscreteRandomVariable):
    def __init__(self, n):
        weights = {i : prod([1 - j / (i + j) for j in range(1, n - i + 1)]) - prod([1 - j / (i + j - 1) for j in range(1, n - i + 2)]) for i in range(1, n + 1)}
        super().__init__(weights)

class X(DiscreteRandomVariable):
    def __init__(self, n):
        super().__init__(((ConstantRandomVariable(n + 1) - P(n)) / ConstantRandomVariable(sqrt(n))).pmf())

if __name__ == '__main__':
    # the probability that a uniformly random permutation of {1,2,3} is ordered at the beginning of the first pass
    print(P(3).cdf(1))
    # the probability that a uniformly random permutation of {1,2,3} is ordered at the beginning of the second pass
    print(P(3).cdf(2))
    # the probability that a uniformly random permutation of {1,2,3} is ordered at the beginning of the third pass
    print(P(3).cdf(3))