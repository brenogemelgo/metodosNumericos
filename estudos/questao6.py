import numpy as np


def f(d):
    return 25 * d**2 + np.log(d) - 1.5e-4


Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100
i = 0

x0 = 0.2
x1 = 0.3

while Epest >= Eppara:

    xr = x1 - (x0 - x1) / (f(x0) - f(x1)) * f(x1)

    if i > 0:
        Epest = abs((xr - x1) / xr) * 100

    x0 = x1
    x1 = xr
    i += 1

print(xr)
print(i)
