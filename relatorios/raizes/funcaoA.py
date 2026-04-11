import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================== #
# GLOBAL


def f(x):
    return np.sin(4 * x) + np.cos(5 * x) + 1 / x


def df(x):
    return 4 * np.cos(4 * x) - 5 * np.sin(5 * x) - 1 / (x**2)


def bisseccao(f, xl, xu, Eppara):
    Epest = 100
    xr_old = 0
    k = 0

    while Epest >= Eppara:
        xr = (xl + xu) / 2

        if (f(xl) * f(xr)) < 0:
            xu = xr
        else:
            xl = xr

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k, Epest


def falsa_posicao(f, xl, xu, Eppara):
    Epest = 100
    xr_old = 0
    k = 0

    while Epest >= Eppara:
        xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

        if (f(xl) * f(xr)) < 0:
            xu = xr
        else:
            xl = xr

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k, Epest


def newton_raphson(f, df, x0, Eppara):
    Epest = 100
    xr_old = x0
    xr = x0
    k = 0

    while Epest >= Eppara:
        xr = xr_old - f(xr_old) / df(xr_old)

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k, Epest


def secante(f, x0, x1, Eppara):
    Epest = 100
    k = 0

    while Epest >= Eppara:
        xr = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))

        if k > 0:
            Epest = abs((xr - x1) / xr) * 100

        x0 = x1
        x1 = xr
        k += 1

    return xr, k, Epest


def secante_modificada(f, x0, Eppara, delta):
    Epest = 100
    xr_old = x0
    k = 0

    while Epest >= Eppara:
        xr = xr_old - delta * xr_old * f(xr_old) / (
            f(xr_old + delta * xr_old) - f(xr_old)
        )

        if k > 0:
            Epest = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        k += 1

    return xr, k, Epest


def imprimir_tabela(df, titulo):
    df_fmt = df.copy()

    for col in df_fmt.columns:
        if col == "Raiz":
            df_fmt[col] = df_fmt[col].map(lambda x: f"{int(x):>4d}")
        elif col == "Iterações":
            df_fmt[col] = df_fmt[col].map(lambda x: f"{int(x):>10d}")
        elif col == "Epest(%)":
            df_fmt[col] = df_fmt[col].map(lambda x: f"{x:>14.6e}")
        else:
            df_fmt[col] = df_fmt[col].map(lambda x: f"{x:>14.10f}")

    print(f"\n{titulo}")
    print(df_fmt.to_string(index=False))


# =============================================================================== #

# =============================================================================== #
# MÉTODO GRÁFICO

n = 1000
x = np.linspace(0.05, 2 * np.pi, n)

plt.figure(figsize=(8, 4.5))
plt.plot(x, f(x), "-b", label="f(x)")
plt.axhline(0, linestyle="--", color="k")
plt.xlim(0, 2 * np.pi)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# =============================================================================== #

# =============================================================================== #
# BUSCA INCREMENTAL

intervalos = [
    [2.5, 3.0],
    [3.0, 3.5],
    [4.0, 4.5],
    [4.5, 5.0],
    [5.0, 5.5],
    [6.0, 6.5],
]

xb = []

for i in range(len(intervalos)):
    xl_global = intervalos[i][0]
    xu_global = intervalos[i][1]

    x_local = np.linspace(xl_global, xu_global, n)

    for k in range(n - 1):
        xl = x_local[k]
        xu = x_local[k + 1]

        if (f(xl) * f(xu)) < 0:
            xb.append([xl, xu])

print("Subintervalos encontrados")
for i in range(len(xb)):
    print(f"I{i+1} = [{xb[i][0]:.10f}, {xb[i][1]:.10f}]")

# =============================================================================== #

# =============================================================================== #
# PARÂMETROS

Eppara = 0.5 * 10 ** (2 - 6)
delta = 0.01

# =============================================================================== #

# =============================================================================== #
# BISSECÇÃO

dados_bisseccao = []

print("\nBISSECÇÃO")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]

    xr, k, Epest = bisseccao(f, xl, xu, Eppara)

    print(f"\nRaiz {i+1}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_bisseccao.append(
        {
            "Raiz": i + 1,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_bisseccao = pd.DataFrame(dados_bisseccao)

# =============================================================================== #

# =============================================================================== #
# FALSA POSIÇÃO

dados_falsa_posicao = []

print("\nFALSA POSIÇÃO")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]

    xr, k, Epest = falsa_posicao(f, xl, xu, Eppara)

    print(f"\nRaiz {i+1}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_falsa_posicao.append(
        {
            "Raiz": i + 1,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_falsa_posicao = pd.DataFrame(dados_falsa_posicao)

# =============================================================================== #

# =============================================================================== #
# NEWTON-RAPHSON

dados_newton = []

print("\nNEWTON-RAPHSON")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]
    x0 = (xl + xu) / 2

    xr, k, Epest = newton_raphson(f, df, x0, Eppara)

    print(f"\nRaiz {i+1}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_newton.append(
        {
            "Raiz": i + 1,
            "x0": x0,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_newton = pd.DataFrame(dados_newton)

# =============================================================================== #

# =============================================================================== #
# SECANTE

dados_secante = []

print("\nSECANTE")
for i in range(len(xb)):
    x0 = xb[i][0]
    x1 = xb[i][1]

    xr, k, Epest = secante(f, x0, x1, Eppara)

    print(f"\nRaiz {i+1}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_secante.append(
        {
            "Raiz": i + 1,
            "x0": x0,
            "x1": x1,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_secante = pd.DataFrame(dados_secante)

# =============================================================================== #

# =============================================================================== #
# SECANTE MODIFICADA

dados_secante_modificada = []

print("\nSECANTE MODIFICADA")
for i in range(len(xb)):
    xl = xb[i][0]
    xu = xb[i][1]
    x0 = (xl + xu) / 2

    xr, k, Epest = secante_modificada(f, x0, Eppara, delta)

    print(f"\nRaiz {i+1}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_secante_modificada.append(
        {
            "Raiz": i + 1,
            "x0": x0,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_secante_modificada = pd.DataFrame(dados_secante_modificada)

# =============================================================================== #

# =============================================================================== #
# TABELAS

imprimir_tabela(df_bisseccao, "TABELA BISSECÇÃO")
imprimir_tabela(df_falsa_posicao, "TABELA FALSA POSIÇÃO")
imprimir_tabela(df_newton, "TABELA NEWTON-RAPHSON")
imprimir_tabela(df_secante, "TABELA SECANTE")
imprimir_tabela(df_secante_modificada, "TABELA SECANTE MODIFICADA")

# =============================================================================== #
# GERAÇÃO DE TABELAS LATEX


# def fmt_decimal(x, casas=10):
#     return f"{x:.{casas}f}".replace(".", ",")


# def fmt_cientifico(x, casas=6):
#     s = f"{x:.{casas}e}"
#     mantissa, expoente = s.split("e")
#     mantissa = mantissa.replace(".", ",")
#     expoente = int(expoente)
#     return f"{mantissa}\\times 10^{{{expoente}}}"


# def linha_metodo(nome_metodo, label_raiz, xr, k, epest, primeira):
#     metodo = nome_metodo if primeira else ""
#     return (
#         f"    {metodo:<20} & $x_{{r,{label_raiz}}}$ & ${fmt_decimal(xr)}$ "
#         f"& ${int(k)}$ & ${fmt_decimal(epest)}$ \\\\"
#     )


# def bloco_metodo(nome_metodo, df, idxs):
#     linhas = []
#     for j, i in enumerate(idxs):
#         linhas.append(
#             linha_metodo(
#                 nome_metodo,
#                 i + 1,
#                 df.loc[i, "xr"],
#                 df.loc[i, "Iterações"],
#                 df.loc[i, "Epest(%)"],
#                 j == 0,
#             )
#         )
#     return "\n".join(linhas)


# def gerar_tabular(idxs, blocos):
#     corpo = "\n    \\midrule\n".join(blocos)

#     return (
#         "\\begin{tabular}{llccc}\n"
#         "    \\toprule\n"
#         "    \\textbf{Método} & \\textbf{Raiz} & \\textbf{$x_r$} & "
#         "\\textbf{Iterações} & \\textbf{$E_{\\text{pest}}$ (\\%)} \\\\\n"
#         "    \\midrule\n"
#         f"{corpo}\n"
#         "    \\bottomrule\n"
#         "\\end{tabular}"
#     )


# # ============================================================================= #
# # USO
# # ============================================================================= #

# raizes_1_3 = [0, 1, 2]
# raizes_4_6 = [3, 4, 5]

# tab_1_3 = gerar_tabular(
#     raizes_1_3,
#     [
#         bloco_metodo("Bissecção", df_bisseccao, raizes_1_3),
#         bloco_metodo("Falsa posição", df_falsa_posicao, raizes_1_3),
#         bloco_metodo("Newton-Raphson", df_newton, raizes_1_3),
#         bloco_metodo("Secante", df_secante, raizes_1_3),
#         bloco_metodo("Secante modificada", df_secante_modificada, raizes_1_3),
#     ],
# )

# tab_4_6 = gerar_tabular(
#     raizes_4_6,
#     [
#         bloco_metodo("Bissecção", df_bisseccao, raizes_4_6),
#         bloco_metodo("Falsa posição", df_falsa_posicao, raizes_4_6),
#         bloco_metodo("Newton-Raphson", df_newton, raizes_4_6),
#         bloco_metodo("Secante", df_secante, raizes_4_6),
#         bloco_metodo("Secante modificada", df_secante_modificada, raizes_4_6),
#     ],
# )

# print(tab_1_3)
# print()
# print(tab_4_6)

# ============================================================================= #

plt.tight_layout()
plt.show()
