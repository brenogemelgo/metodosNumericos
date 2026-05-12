import numpy as np

# primeiro exemplo
A = np.array([[2, 4, -6], [4, 2, 2], [2, 8, -4]])
b = np.array([[10], [16], [24]])

# sistema guardado 1
# A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
# b = np.array([[7.85], [-19.3], [71.4]])

# sistema guardado 2
# A = np.array([[0.0003, 3], [1, 1]])
# b = np.array([[2.0001], [1]])

Aum = np.hstack((A, b))
n = len(b)

# eliminação progressiva
for i in range(n - 1):
    for j in range(i + 1, n):
        fator = Aum[j, i] / Aum[i, i]
        Aum[j, i : n + 1] = Aum[j, i : n + 1] - fator * Aum[i, i : n + 1]

# substituição regressiva
soma = 0
x = np.zeros(n)
x[n - 1] = Aum[n - 1, n] / Aum[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        soma += Aum[i, j] * x[j]
    x[i] = (Aum[i, n] - soma) / Aum[i, i]

print(x)
