import numpy as np

A = np.array([[2, 4, -6], [4, 2, 2], [2, 8, -4]])
b = np.array([[10], [16], [24]])
Aum = np.hstack((A, b))
n = len(b)

# eliminação progressiva
for i in range(n - 1):
    for j in range(i + 1, n):
        fator = Aum[j, i] / Aum[i, i]
        Aum[j, range(i, n + 1)] = (
            Aum[j, range(i, n + 1)] - fator * Aum[i, range(i, n + 1)]
        )

# substituição regressiva
x = np.zeros(n)
x[n - 1] = Aum[n - 1, n] / Aum[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    soma = 0
    for j in range(i + 1, n):
        soma += Aum[i, j] * x[j]
    x[i] = (Aum[i, n] - soma) / Aum[i, i]

print(x)
