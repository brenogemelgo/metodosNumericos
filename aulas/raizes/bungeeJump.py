import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return np.sin(10 * x) + np.cos(3 * x)


i = 3
step = 0.01
x = np.arange(3, 6, 0.01)

xb = []
nb = 0

while i <= 6:
    xl = f(i)
    i += step
    xu = f(i)

    if (xl * xu) < 0:
        nb += 1
        xb.append([xl, xu])

if len(xb) == 0:
    print("Nenhum subintervalo foi encontrado")

print("xb = ", xb)
print("Número de subintervalos = ", nb)

plt.figure()
plt.plot(x, f(x), "-b", label="quero me apaixonar pelo eu-lírico")
plt.show()
