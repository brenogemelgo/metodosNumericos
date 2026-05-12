import numpy as np

A = np.array([[2, 4, -6], [4, 2, 2], [2, 8, -4]])
b = np.array([10, 16, 24])

n = len(b)
x_old = np.zeros(n)
x_new = np.zeros(n)

Eppara = 0.5 * 10 ** (2 - 6)
Epest = 100
k = 0

while Epest >= Eppara:
    for i in range(n):
        soma_A = 0
        soma_B = 0

        for j in range(i):
            if j < i:
                soma_A += A[i, j] * x_new[j]
            elif j > i:
                soma_B += A[i, j] * x_old[j]

        x_new[i] = (b[i] - soma_A - soma_B) / A[i, i]

    x_old = x_new.copy()
    Epest = np.max(np.abs((x_new - x_old) / x_new)) * 100
    k += 1

print(x_new)
