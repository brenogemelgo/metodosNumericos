import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return x**2 / 10 - 2 * np.sin(x)


xl = 0
xu = 4
x = np.linspace(xl, xu, 1000)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.grid()

Eppara = 0.5 * 10 ** (2 - 6)
phi = (1 + math.sqrt(5)) / 2
Ea = 100

while Ea >= Eppara:

    d = (phi - 1) * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    if f(x1) < f(x2):
        xl = x2
        x_opt = x1
    else:
        xu = x1
        x_opt = x2

    Ea = (2 - phi) * abs((xu - xl) / x_opt) * 100

print(x_opt)
plt.axvline(x_opt, linestyle="--")
plt.show()
