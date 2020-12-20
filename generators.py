"""
GENERATOR EXPRESSIONS

Em aulas anteriores, estudamos:
-> list comprehension
-> dictionary comprehension
-> set comprehension

Não vimos:
-> tuple comprehension: porque elas se chamam generators
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
# True
# Apesar de ser generator object, não retorna uma tupla
# Assim como map() e filter(), depois que o dado é usado ele é apagado da memória

"""
Podemo fazer isso usando generators:
"""

print(any(nome[0] == 'C' for nome in nomes))
# True
# OBS.: para ser um list comprehension precisaria ter []

res = ([nome[0] == 'C' for nome in nomes])
print(type(res))  # <class 'list'>
print(res)  # [True, True, True, True, True, False]

print([nome[0] == 'C' for nome in nomes])
# [True, True, True, True, True, False]
# list comprehension

res2 = (nome[0] == 'C' for nome in nomes)
print(type(res2))  # <class 'generator'>
print(res2)  # <generator object <genexpr> at 0x000001F7D614DBA0>

# Generator gasta menos recurso e memória da máquina do que o List comprehension
# O list comprehension imprime a lista em memória e o generator só retorna o geneexpr
# O list comprehension deve ser usado se você precisa da lista para alguma coisa.

from sys import getsizeof  # retorna quantos bytes o elemento passado ocupa em memória

print(getsizeof('Geek'))  # 53 bytes
print(getsizeof('Vivien Rossbach'))  # 64 bytes
print(getsizeof('12345679'))  # 57 bytes
print(getsizeof(True))  # 28 bytes
lista = list(range(1,101))
print(getsizeof(lista))  # 856 bytes

# Gerando uma lista de números com list comprehension:
list_comp = getsizeof([x * 10 for x in range(1000)])

# com set comprehension:
set_comp = getsizeof({x * 10 for x in range(1000)})

# com dict comprehension:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# com generator:
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List comprehension: {list_comp}')
print(f'Set comprehension: {set_comp}')
print(f'Dict comprehension: {dict_comp}')
print(f'Generator: {gen}')

# Para fazer a mesma tarefa gastamos em memória:
# List comprehension: 8856
# Set comprehension: 32984
# Dict comprehension: 36960
# Generator: 112

""" ITERANDO NO GENERATOR EXPRESSION """

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))
# <generator object <genexpr> at 0x000001FB0A84DE40>
# <class 'generator'>

for num in gen:
    print(num)  # imprime de 10 em 10, de 0 a 9990

