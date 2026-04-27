import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100

xl = 3
xu = 6

xr_old = 0
i = 0

while Epest >= Eppara:

    xr = (xl + xu) / 2

    if (f(xl) * f(xr)) < 0:
        xu = xr
    else:
        xl = xr

    if i > 0:
        Epest = abs((xr - xr_old) / xr) * 100

    xr_old = xr
    i += 1


print("Raiz aproximada = ", xr)
print("f(xr) = ", f(xr))
print("Erro estimado = ", Epest)
print("Número de iterações = ", i)
