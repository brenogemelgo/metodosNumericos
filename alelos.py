import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def P(x):
    p, q = x
    return 2 * p + 2 * q - 2 * p**2 - 2 * q**2 - 2 * p * q


def menosP(x):
    return -P(x)


x_true = np.array([1 / 3, 1 / 3])

res = minimize(menosP, x0=[0.25, 0.25])
print(f"p, q = [{res.x[0]:.16f}, {res.x[1]:.16f}]")
print("r = ", 1 - res.x[0] - res.x[1])
print("Pmax =", -res.fun)
print("iterations =", res.nit)
print("estimated error =", np.linalg.norm(res.jac))
print("true error =", np.linalg.norm(res.x - x_true))
