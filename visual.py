import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def experiment(n):
    a = [None] + random.sample(list(range(1, n + 1)), n)
    figure, axis = plt.subplots()
    axis.set_xlim(0, n)
    axis.set_ylim(0, n)
    axis.plot(list(range(n + 1)), list(range(n + 1)), color = 'black')
    point = axis.scatter([], [])
    curve = axis.plot(list(range(n + 1)), [None for i in range(n + 1)])[0]
    threshold = axis.plot([None, None], [0, n], color = 'black')[0]
    border = axis.plot([n, n], [0, n], color = 'grey')[0]
    def update(pas):
        if pas < n:
            t = [x for x in a]
            for i in range(1, pas + 1):
                for j in range(1, n):
                    if t[j] > t[j + 1]:
                        t[j], t[j + 1] = t[j + 1], t[j]
                if t[1 : ] == list(range(1, n + 1)):
                    threshold.set_xdata([n - i + 1, n - i + 1])
                    axis.set_title('pass ${}$ ($P_{{{}}} = {}$)'.format(pas, n, i))
                    break
            if t[1 : ] != list(range(1, n + 1)):
                axis.set_title('pass ${}$ ($P_{{{}}} \geqslant {})$'.format(pas, n, pas))
            point.set_offsets([[i, t[i]] for i in range(n + 1)])
            curve.set_xdata([0] + [i for i in range(1, n + 1) if t[i] == max(t[1 : i + 1])])
            curve.set_ydata([0] + [t[i] for i in range(1, n + 1) if t[i] == max(t[1 : i + 1])])
            border.set_xdata([n - pas + 1, n - pas + 1])
        if pas == n:
            border.set_xdata([1, 1])
        if pas > n:
            border.set_xdata([None, None])
        return point, curve, threshold, border
    animation = FuncAnimation(figure, update, frames = n + 2, repeat = False)
    plt.show()

if __name__ == '__main__':
    experiment(64)