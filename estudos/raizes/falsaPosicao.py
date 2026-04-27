import numpy as np


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100

xl = 3
xu = 6

xr_old = xl
i = 0

while Epest >= Eppara:

    xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

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
