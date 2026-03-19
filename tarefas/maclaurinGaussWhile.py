import numpy as np
import math
import matplotlib.pyplot as plt

# ponto avaliado
x = 1

# número de algarismos significativos
n = 6

# valor verdadeiro
u = math.exp(-(x**2))

# critério de parada de Scarborough
Eppara = 0.5 * 10 ** (2 - n)

# variáveis
soma = 0
old = 0
Ept = 100
Epest = 100
i = 0

estimativa = []
contador = []
EPT = []
EPEST = []


# série de Maclaurin da gaussiana
def MaclaurinGaussiana(x, k):
    return ((-1) ** k) * x ** (2 * k) / math.factorial(k)


# loop principal
while Epest > Eppara:

    # somatório
    soma += MaclaurinGaussiana(x, i)

    # erros percentuais
    Ept = abs((u - soma) / u) * 100
    if i > 0 and soma != 0:
        Epest = abs((soma - old) / soma) * 100
    else:
        Epest = 100

    # valor antigo
    old = soma

    # appends
    estimativa.append(soma)
    contador.append(i)
    EPT.append(Ept)
    EPEST.append(Epest)

    # incremento
    i += 1

# plots
plt.figure()
plt.plot(contador, estimativa, "or", label="estimativa")
plt.axhline(y=u, linestyle="--", label="$e^{-x^2}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

plt.figure()
plt.plot(contador, EPT, "og", label="$E_{pt}$")
plt.plot(contador, EPEST, "ob", label="$E_{pest}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Erros")
plt.grid()

# não precisa fazer isso no spyder. estou usando vscode então preciso
plt.show()
