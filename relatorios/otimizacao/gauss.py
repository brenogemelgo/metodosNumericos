import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-(x**2))


def flinha(x):
    return -2 * x * np.exp(-(x**2))


def flinhalinha(x):
    return -2 * np.exp(-(x**2)) + 4 * x**2 * np.exp(-(x**2))


Epest = 100
Eppara = 0.5 * 10 ** (2 - 6)

xl = 0
xu = 10
n = 1000
x = np.linspace(xl, xu, n)
plt.figure()
plt.plot(x, flinhalinha(x), "-b")
plt.axhline(0, linestyle="--")
i = 0

while Epest >= Eppara:
    xr = (xl + xu) / 2

    if flinhalinha(xl) * flinhalinha(xu) < 0:
        xu = xr
    else:
        xl = xr

    if i > 0:
        Epest = abs((xr - xr_old) / xr) * 100

    xr_old = xr
    i += 1

print(xr)
plt.axvline(xr, linestyle="--")
plt.show()
