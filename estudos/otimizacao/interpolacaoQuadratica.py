import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return x**2 / 10 - 2 * np.sin(x)


x1 = 0
x2 = 1
x3 = 4
x = np.linspace(x1, x3, 1000)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.grid()

Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100
x4_old = x2

while Epest >= Eppara:

    x4_new = x2 - 0.5 * (
        (x2 - x1) ** 2 * (f(x2) - f(x3)) - (x2 - x3) ** 2 * (f(x2) - f(x1))
    ) / ((x2 - x1) * (f(x2) - f(x3)) - (x2 - x3) * (f(x2) - f(x1)))

    Epest = abs((x4_new - x4_old) / x4_new) * 100

    if x4_new > x2:
        if f(x4_new) < f(x2):
            x1 = x2
            x2 = x4_new
        else:
            x3 = x4_new
    else:
        if f(x4_new) < f(x2):
            x3 = x2
            x2 = x4_new
        else:
            x1 = x4_new

    x4_old = x4_new

print(x4_old)
plt.axvline(x4_new, linestyle="--")
plt.show()
