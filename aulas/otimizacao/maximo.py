import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(x):
    return x**2 / 10 - 2 * np.sin(x)


def neg_f(x):
    return -f(x)


x1 = -4
x2 = 0
max = optimize.fminbound(neg_f, x1, x2)
print(max)

x = np.linspace(x1, x2, 1000)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.grid()
plt.axvline(max, linestyle="--")
plt.show()
