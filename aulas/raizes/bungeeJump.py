import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


n = 100
x = np.linspace(3, 6, n)
y = f(x)

xb = []

for i in range(n - 1):
    xl = x[i]
    xu = x[i + 1]

    if (f(xl) * f(xu)) < 0:
        xb.append([xl, xu])

if not xb == 0:
    print("Nenhum subintervalo foi encontrado")

print("xb = ", xb)
print("Número de subintervalos = ", len(xb))

plt.figure()
plt.plot(x, y, "-b", label="f(x)")
plt.axhline(0, linestyle="--")
plt.show()
