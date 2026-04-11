import math
import pandas as pd

# =============================================================================== #
# GLOBAL


def reynolds(rho, V, D, mu):
    return rho * V * D / mu


def blasius(Re):
    return 0.316 / (Re**0.25)


def h(y, eps, D, Re):
    return y + 2 * math.log10(eps / (3.7 * D) + (2.51 / Re) * y)


def dh(y, eps, D, Re):
    termo = eps / (3.7 * D) + (2.51 / Re) * y
    return 1 + (2 / math.log(10)) * (2.51 / Re) / termo


def newton_raphson_colebrook(eps, D, Re, f0, Eppara):
    Epest = 100
    y_old = 1 / math.sqrt(f0)
    k = 0

    while Epest >= Eppara:
        y = y_old - h(y_old, eps, D, Re) / dh(y_old, eps, D, Re)

        if k > 0:
            Epest = abs((y - y_old) / y) * 100

        y_old = y
        k += 1

    f = 1 / (y**2)

    return f, k, Epest


def queda_pressao(f, L, rho, V, D):
    return f * L * rho * V**2 / (2 * D)


def imprimir_tabela_fator(df):
    df_fmt = df.copy()

    df_fmt["Re"] = df_fmt["Re"].map(lambda x: f"{x:.6f}")
    df_fmt["f0"] = df_fmt["f0"].map(lambda x: f"{x:.10f}")
    df_fmt["f"] = df_fmt["f"].map(lambda x: f"{x:.10f}")
    df_fmt["Iterações"] = df_fmt["Iterações"].map(lambda x: f"{x:d}")
    df_fmt["Epest(%)"] = df_fmt["Epest(%)"].map(lambda x: f"{x:.6e}")

    print("\nTABELA FATOR DE ATRITO")
    print(df_fmt.to_string(index=False))


def imprimir_tabela_pressao(df):
    df_fmt = df.copy()

    df_fmt["f"] = df_fmt["f"].map(lambda x: f"{x:.10f}")
    df_fmt["Delta p (Pa)"] = df_fmt["Delta p (Pa)"].map(lambda x: f"{x:.10f}")

    print("\nTABELA QUEDA DE PRESSÃO")
    print(df_fmt.to_string(index=False))


# =============================================================================== #

# =============================================================================== #
# PARÂMETROS

rho = 1.23
mu = 1.79e-5
D = 0.005
V = 40
L = 0.2

Eppara = 0.5 * 10 ** (2 - 6)

Re = reynolds(rho, V, D, mu)
f0 = blasius(Re)

casos = [
    ["Tubo liso", 0.0015e-3],
    ["Aço comercial", 0.045e-3],
]

# =============================================================================== #

# =============================================================================== #
# NEWTON-RAPHSON PARA COLEBROOK

dados_fator = []
dados_pressao = []

print("\nFATOR DE ATRITO E QUEDA DE PRESSÃO")

for i in range(len(casos)):
    caso = casos[i][0]
    eps = casos[i][1]

    f, k, Epest = newton_raphson_colebrook(eps, D, Re, f0, Eppara)
    dp = queda_pressao(f, L, rho, V, D)

    print(f"\n{caso}")
    print(f"Re = {Re:.6f}")
    print(f"f0 = {f0:.10f}")
    print(f"f = {f:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")
    print(f"Delta p (Pa) = {dp:.10f}")

    dados_fator.append(
        {
            "Caso": caso,
            "Re": Re,
            "f0": f0,
            "f": f,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

    dados_pressao.append(
        {
            "Caso": caso,
            "f": f,
            "Delta p (Pa)": dp,
        }
    )

df_fator = pd.DataFrame(dados_fator)
df_pressao = pd.DataFrame(dados_pressao)

# =============================================================================== #

# =============================================================================== #
# TABELAS

imprimir_tabela_fator(df_fator)
imprimir_tabela_pressao(df_pressao)

# =============================================================================== #
