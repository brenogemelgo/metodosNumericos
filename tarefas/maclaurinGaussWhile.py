import math
import time
import numpy as np
import matplotlib.pyplot as plt


# ============================================== FUNÇÕES ============================================== #


# termo explícito da série
def termoMaclaurinExplicito(x, k):
    return ((-1) ** k) * x ** (2 * k) / math.factorial(k)


# relação recursiva da série
def termoMaclaurinGaussiana(x, k, termoAnterior):
    return termoAnterior * (-(x**2)) / k


# ============================================== MÉTODO RECURSIVO ============================================== #


def estimarGaussianaRecursiva(x, n):

    u = math.exp(-(x**2))
    Eppara = 0.5 * 10 ** (2 - n)

    soma = 1.0
    termo = 1.0
    old = soma

    Epest = 100
    i = 0

    estimativa = [soma]
    contador = [0]
    EPT = [abs((u - soma) / u) * 100]
    EPEST = [np.inf]

    while Epest > Eppara:

        i += 1

        termo = termoMaclaurinGaussiana(x, i, termo)
        soma += termo

        Ept = abs((u - soma) / u) * 100
        Epest = abs((soma - old) / soma) * 100 if soma != 0 else 100

        old = soma

        estimativa.append(soma)
        contador.append(i)
        EPT.append(Ept)
        EPEST.append(Epest)

    return contador, estimativa, EPT, EPEST, u


# ============================================== MÉTODO EXPLÍCITO ============================================== #


def estimarGaussianaExplicita(x, n):

    Eppara = 0.5 * 10 ** (2 - n)

    soma = 0
    old = 0

    Epest = 100
    i = 0

    while Epest > Eppara:

        termo = termoMaclaurinExplicito(x, i)
        soma += termo

        Epest = abs((soma - old) / soma) * 100 if soma != 0 else 100
        old = soma
        i += 1

    return soma


# ============================================== TABELA ============================================== #


def tabelaConvergencia(contador, estimativa, EPT, EPEST):

    print("\nTabela de convergência")
    print("k\tEstimativa\t\tEpt(%)\t\tEpest(%)")

    for k, s, ept, epest in zip(contador, estimativa, EPT, EPEST):
        print(f"{k}\t{s:.10f}\t{ept:.6e}\t{epest:.6e}")


# ============================================== EXPORTAÇÃO DAT ============================================== #


def exportarEstimativa(contador, estimativa, nome):

    with open(nome, "w") as f:
        for k, s in zip(contador, estimativa):
            f.write(f"{k} {s}\n")


def exportarErros(contador, EPT, EPEST, nome):

    with open(nome, "w") as f:
        for k, ept, epest in zip(contador, EPT, EPEST):
            f.write(f"{k} {ept} {epest}\n")


# ============================================== PROGRAMA PRINCIPAL ============================================== #

valores_x = [1, 2]

n = 6


for x in valores_x:

    print("\n==============================================")
    print(f"x = {x}")
    print("==============================================")

    # recursivo
    t0 = time.perf_counter()
    contador, estimativa, EPT, EPEST, u = estimarGaussianaRecursiva(x, n)
    t1 = time.perf_counter()

    tempo_rec = t1 - t0

    # explícito
    t0 = time.perf_counter()
    estimarGaussianaExplicita(x, n)
    t1 = time.perf_counter()

    tempo_exp = t1 - t0

    # tabela
    tabelaConvergencia(contador, estimativa, EPT, EPEST)

    # dumps para tikz
    exportarEstimativa(contador, estimativa, f"estimativa_x{x}.dat")
    exportarErros(contador, EPT, EPEST, f"erros_x{x}.dat")

    # tempos
    print("\nTempos de execução")
    print(f"Explícito : {tempo_exp:.6e} s")
    print(f"Recursivo : {tempo_rec:.6e} s")

    # ============================================== SUBPLOTS ============================================== #

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
    axs[1].set_ylabel("Erro (%)")
    axs[1].legend()
    axs[1].grid()

    plt.tight_layout()

plt.show()
