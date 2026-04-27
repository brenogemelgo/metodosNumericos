import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


n = 1000
x = np.linspace(3, 6, n)
xb = []

for k in range(n - 1):

    xl = x[k]
    xu = x[k + 1]

    if (f(xl) * f(xu)) < 0:
        xb.append([xl, xu])

xn = len(xb)

if xn == 0:
    print("Nenhum subintervalo foi encontrado")

print("xb = ", xb)
print("Número de subintervalos = ", xn)
