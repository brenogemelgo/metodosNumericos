import numpy as np
import matplotlib.pyplot as plt

# =============================================================================== #
# GLOBAL


def f(x):
    return x**2 - 2


def bisseccao(f, xl, xu, Eppara):
    Epest = 100
    xr_old = 0
    k = 0

    while Epest >= Eppara:
        xr = (xl + xu) / 2

        if (f(xl) * f(xr)) < 0:
            xu = xr
        else:
            xl = xr

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k


def falsa_posicao(f, xl, xu, Eppara):
    Epest = 100
    xr_old = 0
    k = 0

    while Epest >= Eppara:
        xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

        if (f(xl) * f(xr)) < 0:
            xu = xr
        else:
            xl = xr

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k


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
# BISSECÇÃO E FALSA POSIÇÃO

Eppara = 0.5 * 10 ** (2 - 6)

print("\nBISSECÇÃO")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]

    xr, k = bisseccao(f, xl, xu, Eppara)

    print(f"Intervalo {i+1}: [{xl}, {xu}]")
    print("Raiz encontrada =", xr)
    print("Iterações =", k)
    print()

print("FALSA POSIÇÃO")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]

    xr, k = falsa_posicao(f, xl, xu, Eppara)

    print(f"Intervalo {i+1}: [{xl}, {xu}]")
    print("Raiz encontrada =", xr)
    print("Iterações =", k)
    print()

# =============================================================================== #

plt.show()
