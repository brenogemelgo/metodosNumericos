import numpy as np
import matplotlib.pyplot as plt

# =============================================================================== #
# GLOBAL


def f(x):
    return x**2 - 2


# =============================================================================== #

# =============================================================================== #
# MÉTODO GRÁFICO
n = 1000
x = np.linspace(-2, 2, n)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.axhline(0, linestyle="--")

# =============================================================================== #

# =============================================================================== #
# BUSCA INCREMENTAL

xb = []
for k in range(n - 1):
    xl = x[k]
    xu = x[k + 1]

    if (f(xl) * f(xu)) < 0:
        xb.append([xl, xu])

print("Intervalos")
print(xb)
# =============================================================================== #

# =============================================================================== #
# FALSA POSIÇÃO

Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100
xr_old = 0
k = 0
while Epest >= Eppara:

    # bisecção
    # xr = (xl + xu) / 2

    xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

    if (f(xl) * f(xr)) < 0:
        xu = xr
    else:
        xl = xr

    Epest = abs((xr - xr_old) / xr)

    xr_old = xr
    k += 1

print("Raiz encontrada")
print(xr)

# =============================================================================== #

plt.show()
