import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

# Dados Iniciais
r = 2  # m
L = 5  # m
V = 8  # m^3


# Critério de Parada de Scarvorought (1966)
n = 6
Eppara = 0.5 * 10 ** (2 - n)


# Equação do cálculo de h de um líquido em um cilindro horizontal
def f(h):

    return (
        V - (r**2 * math.acos((r - h) / r) - (r - h) * math.sqrt(2 * r * h - h**2)) * L
    )


# Método da Secante Modificado
delta = 0.01
h_old = (0.55 + 1.86) / 2

Epest = 100.0
k = 0
maxiter = 1000

EPEST = [Epest]
K = [k]
H = [h_old]

while Epest > Eppara or k > maxiter:

    h_new = h_old - delta * h_old * f(h_old) / (f(h_old + delta * h_old) - f(h_old))

    Epest = abs((h_new - h_old) / h_new) * 100

    h_old = h_new
    k += 1

    EPEST.append(Epest)
    K.append(k)
    H.append(h_new)

# Dataframe
dados = {"Iteração": K, "h": H, "Epest": EPEST}

Dados = pd.DataFrame(dados)
print(Dados)
# Gráficos
plt.plot(Dados["Iteração"], Dados["Epest"], "or", label="$E_{pest}$")
plt.xlabel("Iterações")
plt.ylabel("$E_{pest}$ (%)")
plt.grid()
plt.show()

plt.plot(Dados["Iteração"], Dados["h"], "or", label="$V$")
plt.xlabel("Iterações")
plt.ylabel("$h$ (m)")
plt.grid()
plt.show()
