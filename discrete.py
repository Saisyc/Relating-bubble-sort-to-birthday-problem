import matplotlib.pyplot as plt

class DiscreteRandomVariable:
    def __init__(self, weights):
        weights = {float(i) : float(weights[i]) for i in weights.keys() if weights[i] > 0}
        summation = sum(weights.values())
        self.__pmf = {i : weights[i] / summation for i in weights.keys()}
    def pmf(self, x = None):
        if x == None:
            return self.__pmf
        else:
            x = float(x)
            return self.__pmf[x] if x in self.__pmf.keys() else 0
    def cdf(self, x = None):
        if x == None:
            cdf = {}
            summation = 0
            for i in sorted(list(self.__pmf.keys())):
                summation += self.__pmf[i]
                cdf[i] = summation
            return cdf
        else:
            x = float(x)
            summation = 0
            for i in sorted(list(self.__pmf.keys())):
                if i > x:
                    break
                summation += self.__pmf[i]
            return summation
    def expectation(self):
        return sum([self.__pmf[i] * i for i in self.__pmf.keys()])
    def variance(self):
        return sum([self.__pmf[i] * i ** 2 for i in self.__pmf.keys()]) - sum([self.__pmf[i] * i for i in self.__pmf.keys()]) ** 2
    def moment(self, k):
        return sum([self.__pmf[i] * i ** k for i in self.__pmf.keys()])
    def plot(self, color = None):
        x = sorted(list(self.__pmf.keys()))
        y = [self.__pmf[i] for i in x]
        plt.scatter(x, y, color = color)

class ConstantRandomVariable(DiscreteRandomVariable):
    def __init__(self, value):
        super().__init__({value : 1})

if __name__ == '__main__':
    # P{W=1} : P{W=2} : P{W=3} = 1 : 3 : 2
    drv = DiscreteRandomVariable({1 : 1, 2 : 3, 3 : 2})
    # P{W=1} = 1/6, P{W=2} = 3/6, P{W=3} = 2/6
    print(drv.pmf())
    # P{W=2.2} = 0/6
    print(drv.pmf(2.2))
    # P{W≤1} = 1/6, P{W≤2} = 4/6, P{W≤3} = 6/6
    print(drv.cdf())
    # P{W≤2.2} = 4/6
    print(drv.cdf(2.2))
    # E(W) = 13/6
    print(drv.expectation())
    # V(W) = 17/36
    print(drv.variance())
    # E(W^2) = 31/6
    print(drv.moment(2))
    # E(W^3) = 79/6
    print(drv.moment(3))
    # plot probability mass function of W
    drv.plot()
    plt.show()