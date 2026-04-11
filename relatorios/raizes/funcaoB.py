import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================== #
# GLOBAL


def f(x):
    return np.sin(x) + np.cos(1 + x**2) - 1


def secante(f, xim1, xi, Eppara):
    Epest = 100
    k = 0

    while Epest >= Eppara:
        xr = xi - f(xi) * (xim1 - xi) / (f(xim1) - f(xi))

        if k > 0:
            Epest = abs((xr - xi) / xr) * 100

        xim1 = xi
        xi = xr
        k += 1

    return xr, k, Epest


def imprimir_tabela(df):
    df_fmt = df.copy()

    df_fmt["x(i-1)"] = df_fmt["x(i-1)"].map(lambda x: f"{x:.10f}")
    df_fmt["x(i)"] = df_fmt["x(i)"].map(lambda x: f"{x:.10f}")
    df_fmt["xr"] = df_fmt["xr"].map(lambda x: f"{x:.10f}")
    df_fmt["Iterações"] = df_fmt["Iterações"].map(lambda x: f"{x:d}")
    df_fmt["Epest(%)"] = df_fmt["Epest(%)"].map(lambda x: f"{x:.6e}")

    print("\nTABELA SECANTE")
    print(df_fmt.to_string(index=False))


# =============================================================================== #

# =============================================================================== #
# MÉTODO GRÁFICO

n = 1000
x = np.linspace(0, 3.2, n)

plt.figure()
plt.plot(x, f(x), "-b", label="f(x)")
plt.axhline(0, linestyle="--")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# =============================================================================== #

# =============================================================================== #
# SECANTE

Eppara = 0.5 * 10 ** (2 - 6)

casos = [
    ["a", 1.0, 3.0],
    ["b", 1.5, 2.5],
    ["c", 1.5, 2.25],
]

dados_secante = []

print("\nSECANTE")
for i in range(len(casos)):
    caso = casos[i][0]
    xim1 = casos[i][1]
    xi = casos[i][2]

    xr, k, Epest = secante(f, xim1, xi, Eppara)

    print(f"\nCaso {caso}")
    print(f"x(i-1) = {xim1}")
    print(f"x(i)   = {xi}")
    print(f"Raiz encontrada = {xr:.10f}")
    print(f"Iterações = {k}")
    print(f"Epest (%) = {Epest:.6e}")

    dados_secante.append(
        {
            "Caso": caso,
            "x(i-1)": xim1,
            "x(i)": xi,
            "xr": xr,
            "Iterações": k,
            "Epest(%)": Epest,
        }
    )

df_secante = pd.DataFrame(dados_secante)

# =============================================================================== #

# =============================================================================== #
# TABELA

imprimir_tabela(df_secante)

# =============================================================================== #

plt.show()
