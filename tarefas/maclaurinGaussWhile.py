import numpy as np
import math
import matplotlib.pyplot as plt


# ============================================== FUNÇÕES ============================================== #


# relação recursiva para estimar a gaussiana a partir da série de Maclaurin
def termoMaclaurinGaussiana(x, k, termoAnterior):
    return termoAnterior * (-(x**2)) / k


# função iterativa para estimar a gaussiana
def estimarGaussiana(x, n):

    # valor verdadeiro
    u = math.exp(-(x**2))

    # critério de Scarborough
    Eppara = 0.5 * 10 ** (2 - n)

    # variáveis
    soma = 1.0
    termo = 1.0
    old = soma

    Epest = 100
    i = 0

    # listas
    estimativa = [soma]
    contador = [0]
    EPT = [abs((u - soma) / u) * 100]
    EPEST = [100]

    # loop principal
    while Epest > Eppara:

        i += 1

        termo = termoMaclaurinGaussiana(x, i, termo)
        soma += termo

        Ept = abs((u - soma) / u) * 100
        if soma != 0:
            Epest = abs((soma - old) / soma) * 100
        else:
            Epest = 100

        old = soma

        estimativa.append(soma)
        contador.append(i)
        EPT.append(Ept)
        EPEST.append(Epest)

    # retorna valores
    return contador, estimativa, EPT, EPEST, u


# ============================================== PROGRAMA PRINCIPAL ============================================== #

# valores de x para estimativas
valores_x = [-2, 2]

# número de algarismos significativos
n = 6

for x in valores_x:

    contador, estimativa, EPT, EPEST, u = estimarGaussiana(x, n)
    fig, axs = plt.subplots(2, 1, figsize=(6, 8))

    # estimativa
    axs[0].plot(contador, estimativa, "or", label="estimativa")
    axs[0].axhline(y=u, linestyle="--", label="$e^{-x^2}$")
    axs[0].set_title(f"Aproximação da Gaussiana (x = {x})")
    axs[0].set_xlabel("Número de termos")
    axs[0].set_ylabel("Estimativa")
    axs[0].legend()
    axs[0].grid()

    # erros
    axs[1].plot(contador, EPT, "og", label="$E_{pt}$")
    axs[1].plot(contador, EPEST, "ob", label="$E_{pest}$")
    axs[1].set_title(f"Erros para x = {x}")
    axs[1].set_xlabel("Número de termos")
    axs[1].set_yscale("log")
    axs[1].set_ylabel("Erro (%)")
    axs[1].legend()
    axs[1].grid()

    plt.tight_layout()

plt.show()
