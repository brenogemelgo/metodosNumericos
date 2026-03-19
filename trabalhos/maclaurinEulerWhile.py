import math
import time
import numpy as np
import matplotlib.pyplot as plt


# termo geral da série
def termoSerie(k):
    return 1 / (k**4)


# rotina principal
def estimarSerie(n):

    u = (math.pi**4) / 90
    Eppara = 0.5 * 10 ** (2 - n)

    soma = 0.0
    old = 0.0

    Ept = 100
    Epest = 100
    i = 1

    estimativa = []
    contador = []
    EPT = []
    EPEST = []

    while Ept > Eppara:

        soma += termoSerie(i)

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

        i += 1

    return contador, estimativa, EPT, EPEST, u


# ============================================== TABELA ============================================== #


def tabelaConvergencia(contador, estimativa, EPT, EPEST):

    print("\nTabela de convergência")
    print("i\tEstimativa\t\tEpt(%)\t\tEpest(%)")

    for i, s, ept, epest in zip(contador, estimativa, EPT, EPEST):
        print(f"{i}\t{s:.10f}\t{ept:.6e}\t{epest:.6e}")


# ============================================== EXPORTAÇÃO DAT ============================================== #


def exportarEstimativa(contador, estimativa, nome):

    with open(nome, "w") as f:
        for i, s in zip(contador, estimativa):
            f.write(f"{i} {s}\n")


def exportarErros(contador, EPT, EPEST, nome):

    with open(nome, "w") as f:
        for i, ept, epest in zip(contador, EPT, EPEST):
            f.write(f"{i} {ept} {epest}\n")


# ============================================== PROGRAMA PRINCIPAL ============================================== #

n = 6

t0 = time.perf_counter()
contador, estimativa, EPT, EPEST, u = estimarSerie(n)
t1 = time.perf_counter()

tempo_exp = t1 - t0

# tabela
tabelaConvergencia(contador, estimativa, EPT, EPEST)

# dumps para plotar no tikz
exportarEstimativa(contador, estimativa, "estimativa_q2.dat")
exportarErros(contador, EPT, EPEST, "erros_q2.dat")

# resultado final
print("\nResultado final")
print(f"Valor exato        : {u:.10f}")
print(f"Última estimativa  : {estimativa[-1]:.10f}")
print(f"Número de termos   : {contador[-1]}")

# tempo
print("\nTempo de execução")
print(f"t : {tempo_exp:.6e} s")

# ============================================== SUBPLOTS ============================================== #

fig, axs = plt.subplots(2, 1, figsize=(6, 8))

# estimativa
axs[0].plot(contador, estimativa, "or", label="estimativa")
axs[0].axhline(y=u, linestyle="--", label=r"$\pi^4/90$")
axs[0].set_title("Aproximação da série $\sum 1/i^4$")
axs[0].set_xlabel("Número de termos")
axs[0].set_ylabel("Estimativa")
axs[0].legend()
axs[0].grid()

# erros
axs[1].plot(contador, EPT, "og", label=r"$E_{pt}$")
axs[1].plot(contador, EPEST, "ob", label=r"$E_{pest}$")
axs[1].set_title("Erros da série $\sum 1/i^4$")
axs[1].set_xlabel("Número de termos")
axs[1].set_ylabel("Erro (%)")
axs[1].legend()
axs[1].grid()

plt.tight_layout()
plt.show()
