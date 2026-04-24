import numpy as np
import matplotlib.pyplot as plt

n = 1000
x1 = np.linspace(-2, 0, n)
x2 = np.linspace(0, 3, n)
X1, X2 = np.meshgrid(x1, x2)
f = 2 + X1 - X2 + 2 * X1**2 + 2 * X1 * X2 + X2**2

plt.figure()
ax = plt.axes(projection="3d")
cs = ax.plot_surface(X1, X2, f, cmap="viridis")

plt.figure()
plt.contour(X1, X2, f, cmap="viridis")

plt.show()
