"""
DICTIONARY COMPREHENSION

--> Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

--> Se quisermos criar uma tupla:
tupla = 1,2,3,4

--> Se quisermos criar um set:
conjunto = {1,2,3,4}

--> Se quisermos criar um dicionário:

dicionario = {'a':1, 'b':2, 'c':3, 'd':4}

SINTAXE:

{chave: valor for valor in iteravel}

LISTA:
[valor for valor in iteravel]
"""

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)
# {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}

numeros = [1, 2, 3, 4, 5, 1, 2]  # se fosse um set ou tupla quadrados funcionaria também

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# OBS.: não há repetição de chaves

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# EXEMPLO COM LÓGICA CONDICIONAL:

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
# {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}

