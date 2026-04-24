import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(x):
    return x**2 / 10 - 2 * np.sin(x)


x1 = 0
x2 = 4
min = optimize.fminbound(f, x1, x2)
print(min)

x = np.linspace(x1, x2, 1000)
plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.grid()
plt.axvline(min, linestyle="--")
plt.show()
