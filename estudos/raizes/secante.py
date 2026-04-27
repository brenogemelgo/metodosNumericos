import numpy as np


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100

x0 = 3
x1 = 6

k = 0

while Epest >= Eppara:
    xr = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))

    if k > 0:
        Epest = abs((xr - x1) / xr) * 100

    x0 = x1
    x1 = xr
    k += 1


print("Raiz aproximada = ", xr)
print("f(xr) = ", f(xr))
print("Erro estimado = ", Epest)
print("Número de iterações = ", k)
