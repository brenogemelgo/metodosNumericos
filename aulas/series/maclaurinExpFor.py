import numpy as np
import math
import matplotlib.pyplot as plt

# e^x
x = 1

# número de algarismos significativos
n = 6

# exponencial de x
u = math.exp(x)

# definição de valores
soma = 0
old = 0
estimativa = []
contador = []
EPT = []
EPEST = [100]


# série de Maclaurin
def Maclaurin(x, n):
    return x**n / math.factorial(n)


# loop principal
for i in range(n):

    # somatório
    soma = soma + Maclaurin(x, i)

    # erros percentuais
    Ept = abs((u - soma) / u) * 100
    if i > 0:
        Epest = abs((soma - old) / soma) * 100
        EPEST.append(Epest)

    # valor antigo
    old = soma

    # appends
    estimativa.append(soma)
    contador.append(i)
    EPT.append(Ept)

plt.figure()
plt.plot(contador, estimativa, "or", label="$\mathrm{e}^x$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

plt.figure()
plt.plot(contador, EPT, "og", label="$E_{\\text{pt}}$")
plt.plot(contador, EPEST, "ob", label="$E_{\\text{pest}}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Erros")
plt.grid()

plt.show()
