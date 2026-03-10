import math
import os

# limpa o console antes da execução
os.system("cls" if os.name == "nt" else "clear")

# valor de x para o qual queremos calcular e^x
x = 1

# número de algarismos significativos desejados
n = 6

# critério de parada de Scarborough (o Diego escreve errado)
# garante pelo menos n algarismos significativos corretos
Eppara = 0.5 * 10 ** (2 - n)

# valor "verdadeiro" de e^x calculado usando a biblioteca 'math'
# será usado apenas para comparar o erro real
valor_real = math.exp(x)

# primeiro termo da série de Maclaurin de e^x
# quando i = 0 temos: x^0 / 0! = 1
# precisamos inicializar esse termo antes do loop para que a soma da série comece com um valor definido
termo = 1

# approx guarda a soma parcial da série
# ou seja, a aproximação atual de e^x
approx = termo

# approx_old guarda a aproximação da iteração anterior
# será usado para calcular o erro percentual estimado
approx_old = termo

# erro percentual estimado entre duas iterações consecutivas
# começa grande para garantir que o loop execute!
# se inicializar como zero, Epest > Eppara nunca vai ser verdadeiro
Epest = float("inf")

# contador de termos da série (começa em i = 1)
i = 1

# cabeçalho da tabela (títulos pra cada coluna de resultado)
print("Iter\t\tAproximacao\t\tEpest (%)\t\tEprv (%)")
print("-" * 80)

# continua somando termos da série enquanto o erro estimado
# for maior que o erro permitido pelo critério de Scarborough
while Epest > Eppara:

    # calcula o próximo termo da série
    termo = x**i / math.factorial(i)

    # atualiza a soma parcial da série
    approx = approx + termo

    # erro percentual estimado
    Epest = abs((approx - approx_old) / approx) * 100

    # erro percentual relativo verdadeiro
    Eprv = abs((valor_real - approx) / valor_real) * 100

    # imprime resultados da iteração
    print(f"{i}\t\t{approx:.10f}\t\t{Epest:.10f}\t\t{Eprv:.10f}")

    # atualiza a aproximação anterior para a próxima iteração
    approx_old = approx

    # avança para o próximo termo da série
    i += 1

# resultados finais
print("-" * 80)
print(f"{'Valor verdadeiro'}: {valor_real:.10f}")
print(f"{'Aproximacao final'}: {approx:.10f}")
print("Numero de iteracoes:", i - 1)
print("Numero de termos:", i)
