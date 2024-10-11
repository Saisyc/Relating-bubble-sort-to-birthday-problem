import sympy
import math
import matplotlib.pyplot as plt
from numpy import prod

def factorial(n, symbolized = False):
    if symbolized:
        return sympy.sqrt(2 * sympy.pi * n) * (n / sympy.E) ** n * sympy.exp(1 / (12 * n))
    else:
        return math.sqrt(2 * math.pi * n) * (n / math.e) ** n * math.exp(1 / (12 * n))

def logarithmfFactorial(n, symbolized = False):
    if symbolized:
        return n * sympy.log(n) - n + 1 / (12 * n) + sympy.log(2 * sympy.pi * n) / 2
    else:
        return n * math.log(n) - n + 1 / (12 * n) + math.log(2 * math.pi * n) / 2

def bubbleCDF(x, n, symbolized = False):
    if symbolized:
        return 1 - sympy.exp(logarithmfFactorial(n - x * sympy.sqrt(n), symbolized) - logarithmfFactorial(n, symbolized) + (x * sympy.sqrt(n)) * sympy.log(n - x * sympy.sqrt(n)))
    else:
        return 1 - math.exp(logarithmfFactorial(n - x * math.sqrt(n), symbolized) - logarithmfFactorial(n, symbolized) + (x * math.sqrt(n)) * math.log(n - x * math.sqrt(n)))

def bubblePMF(x, n, symbolized = False):
    if symbolized:
        return bubbleCDF(x, n, symbolized) - bubbleCDF(x - 1 / sympy.sqrt(n), n, symbolized)
    else:
        return bubbleCDF(x, n, symbolized) - bubbleCDF(x - 1 / math.sqrt(n), n, symbolized)

def bubbleMoment():
    raise

def birthdayCDF(x, n, symbolized = False):
    if symbolized:
        return 1 - sympy.exp(logarithmfFactorial(n, symbolized) - logarithmfFactorial(n - x * sympy.sqrt(n) - 1, symbolized) - (x * sympy.sqrt(n) + 1) * sympy.log(n))
    else:
        return 1 - math.exp(logarithmfFactorial(n, symbolized) - logarithmfFactorial(n - x * math.sqrt(n) - 1, symbolized) - (x * math.sqrt(n) + 1) * math.log(n))

def birthdayPMF(x, n, symbolized = False):
    if symbolized:
        return birthdayCDF(x, n, symbolized) - birthdayCDF(x - 1 / sympy.sqrt(n), n, symbolized)
    else:
        return birthdayCDF(x, n, symbolized) - birthdayCDF(x - 1 / math.sqrt(n), n, symbolized)

def birthdayMoment():
    raise

def integral(f, x, v):
    f /= sympy.exp(- x ** 2 / 2)
    f = sympy.Poly(f.series(v, 0, 6).removeO().expand(), x)
    g = 0
    for term in f.terms():
        if term[0][0] % 2 == 0:
            g += sympy.sympify(term[1]) * round(prod([i for i in range(1, term[0][0] + 1, 2)])) * sympy.sqrt(sympy.pi / 2)
        else:
            g += sympy.sympify(term[1]) * round(prod([i for i in range(2, term[0][0] + 1, 2)]))
    g = g.series(v, 0, 6).removeO()
    return g

def summation(f, k, x, v):
    if k == 2:
        return sympy.collect((integral(f * x ** 2, x, v) / v + v ** 4 / 120).simplify(), v)
    else:
        return sympy.collect((integral(f * x ** k, x, v) / v).simplify(), v)

def approximation(f):
    if f in [bubbleCDF, birthdayCDF]:
        return lambda x, v, symbolized = False: 1 - sympy.exp(- x ** 2 / 2) * sympy.exp(sympy.collect(sympy.log((1 - f(x, 1 / v ** 2, symbolized = True)) / sympy.exp(- x ** 2 / 2)).series(v, 0, 6).removeO().simplify().series(v, 0, 5).removeO(), v)) if symbolized else float((1 - sympy.exp(- x ** 2 / 2) * sympy.exp(sympy.collect(sympy.log((1 - f(x, 1 / v ** 2, symbolized = True)) / sympy.exp(- x ** 2 / 2)).series(v, 0, 6).removeO().simplify().series(v, 0, 5).removeO(), v))).evalf())
    if f in [bubblePMF, birthdayPMF]:
        return lambda x, v, symbolized = False: sympy.exp(- x ** 2 / 2) * sympy.exp(sympy.collect(sympy.log(f(x, 1 / v ** 2, symbolized = True) / sympy.exp(- x ** 2 / 2)).series(v, 0, 5).removeO().simplify().series(v, 0, 4).removeO(), v)) if symbolized else float((sympy.exp(- x ** 2 / 2) * sympy.exp(sympy.collect(sympy.log(f(x, 1 / v ** 2, symbolized = True) / sympy.exp(- x ** 2 / 2)).series(v, 0, 5).removeO().simplify().series(v, 0, 4).removeO(), v))).evalf())
    pmf = {bubbleMoment : bubblePMF, birthdayMoment : birthdayPMF}
    if f in pmf.keys():
        x = sympy.symbols('x')
        v = sympy.symbols('v')
        return lambda k, n, symbolized = False: summation(pmf[f](x, 1 / v ** 2, symbolized = True), k, x, v).subs(v, 1 / sympy.sqrt(n)) if symbolized else float(summation(pmf[f](x, 1 / v ** 2, symbolized = True), k, x, v).subs(v, 1 / sympy.sqrt(n)).evalf())

def display(f, k = None):
    x = sympy.symbols('x')
    v = sympy.symbols('v')
    n = sympy.symbols('n')
    if k == None:
        g = f(x, v, symbolized = True).subs(v, 1 / sympy.sqrt(n))
    else:
        g = f(k, n, symbolized = True)
        print(g)
    plt.text(1 / 2, 1 / 2, '${}$'.format(sympy.latex(g)), ha = 'center', va = 'center')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    # approximation of the first moment of X(n)
    display(approximation(bubblePMF))
    raise
    # approximation of the second moment of X(n)
    dispshow(bubblePMF, 2)
    print(calculate(bubblePMF, n, 2))
    # approximation of the third moment of X(n)
    dispshow(bubblePMF, 3)
    print(calculate(bubblePMF, n, 3))
    # approximation of the first moment of Z(n)
    dispshow(birthdayPMF, 1)
    print(calculate(birthdayPMF, n, 1))
    # approximation of the second moment of Z(n)
    dispshow(birthdayPMF, 2)
    print(calculate(birthdayPMF, n, 2))
    # approximation of the third moment of Z(n)
    dispshow(birthdayPMF, 3)
    print(calculate(birthdayPMF, n, 3))