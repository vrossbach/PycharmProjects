"""
LISTAS ANINHADAS

--> Algumas linguagens de programação (C, Java, PHP)
possuem estruturas de dados chamadas de arrays, que podem ser:
    --> unidimensionais (arrays/vetores)
    --> multidimensionais (matrizes)

--> No Python não existem arrays, mas sim listas

--> Nos arrays só podemos ter um tipo de dado e em listas podemos
    ter tipos misturados.

--> LISTAS ALINHADAS ou LISTED LISTS são os ARRAYS MULTIDIMENSIONAIS

--> São muito usadas em data science
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)
print(type(listas))

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# <class 'list'>

# Como acessar os dados?

print(listas[0])  # [1, 2, 3]

print(listas[0][1])  # elemento da linha zero e coluna 1: 2

# ìndices negativos (círculo):
print(listas[-2][1])  # 5

# Iterando com loops em uma lista aninhada:
for lista in listas:
    print(lista)
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
for lista in listas:
    for numero in lista:
        print(numero)
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9

# List comprehension:

[[print(valor) for valor in lista] for lista in listas]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Gerando um tabuleiro ou matriz 3x3:

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Gerando jogadas para o jogo da velha:

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# [['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]

# Tabuleiro zerado:
print([['*' for i in range(1, 4)] for j in range(1, 4)])
# [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
