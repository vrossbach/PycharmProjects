"""
ZIP

zip() --> cria um iterável chamado (Zip Object) que agrega elementos de cada
          um dos iteráveis passados como entrada em pares.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# <zip object at 0x0000014A7F0CD340>
# <class 'zip'>

from sys import getsizeof

print(getsizeof(zip1))  # 56
print(getsizeof(lista1))  # 120
print(getsizeof(lista2))  # 120

# Sempre podemos gerar uma lista, tupla, set ou dicionário:

print(list(zip1))
# [(1, 4), (2, 5), (3, 6)] --> lista contendo tuplas
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))
# ((1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c'))
zip1 = zip(lista1, lista2)
print(set(zip1))
# {(2, 5), (1, 4), (3, 6)}
zip1 = zip(lista1, lista2)
print(dict(zip1))
# {1: 4, 2: 5, 3: 6}

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# O zip usa como parâmetro o menor tamanho em iterável.
# Se os iteráveis tiverem tamanhos diferentes, o zip pára
# quando os elementos do menor iterável acabarem, não importa a ordem.

zip1 = zip(lista3, lista2, lista1)
print(list(zip1))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

# Podemos utilizar diferentes iteráveis com zip()
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))
# [(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]
zt = zip(tupla, lista, dicionario.values())
print(tuple(zt))
# ((1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15))

dados = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip(*dados)))  # desempacota
# [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
# {'maria': 98, 'pedro': 91, 'carla': 78}

# Podemos usar o map():
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
# {'maria': 98, 'pedro': 91, 'carla': 78}