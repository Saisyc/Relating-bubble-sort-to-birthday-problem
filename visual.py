import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def f(n):
    a = [None] + random.sample(list(range(1, n + 1)), n)
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.plot(list(range(n + 1)), list(range(n + 1)), color = 'black')
    sc = ax.scatter([], [])
    pl = ax.plot(list(range(n + 1)), [None for i in range(n + 1)])[0]
    bo = ax.plot([n, n], [0, n], color = 'red')[0]
    def update(frame):
        t = [x for x in a]
        for i in range(1, frame + 1):
            for j in range(1, n):
                if t[j] > t[j + 1]:
                    t[j], t[j + 1] = t[j + 1], t[j]
            if t[1 : ] == list(range(1, n + 1)):
                bo.set_xdata([n - i + 1, n - i + 1])
                ax.set_title('pass ${}$\n$P_{{{}}} = {}$'.format(frame, n, i))
                break
        if t[1 : ] != list(range(1, n + 1)):
            ax.set_title('pass ${}$\n$P_{{{}}} \geqslant {}$'.format(frame, n, frame))
            bo.set_xdata([n - frame + 1, n - frame + 1])
        sc.set_offsets([[i, t[i]] for i in range(n + 1)])
        pl.set_xdata([0] + [i for i in range(1, n + 1) if t[i] == max(t[1 : i + 1])])
        pl.set_ydata([0] + [t[i] for i in range(1, n + 1) if t[i] == max(t[1 : i + 1])])
        return sc, pl, bo
    ani = FuncAnimation(fig, update, frames = n, repeat = False)
    plt.show()

f(100)