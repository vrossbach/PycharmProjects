"""
LIST COMPREHENSION

- Nós podemos adicionar estruturas condicionais lógicas às no ssas List Comprehensions
"""

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

pares = [numero for numero in numeros if not numero % 2]
# Obs.: %2 para pares é zero e zero é False (por isso if not)

impares = [numero for numero in numeros if numero % 2]
# Obs.: % 2 para ímpares é 1 = True

print(pares)
print(impares)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)
# [0.5, 4, 1.5, 8, 2.5, 12]
