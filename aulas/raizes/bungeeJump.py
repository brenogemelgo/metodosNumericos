import numpy as np


def f(m):
    return np.sqrt(9.81 * m / 0.25) * np.tanh(np.sqrt(9.81 * 0.25 / m) * 4) - 36


u = 142.7376

Eppara = 0.5 * 10 ** (2 - 6)
Ept = 100
Epest = 100

xl = 140
xu = 150

xr_old = 0

k = 0
while Epest >= Eppara:

    # bissecção
    # xr = (xl + xu) / 2

    # falsa posição
    xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

    if (f(xl) * f(xr)) < 0:
        xu = xr
    else:
        xl = xr

    Ept = abs((u - xr) / u) * 100
    Epest = abs((xr - xr_old) / xr)

    xr_old = xr
    k += 1

print(xr)
