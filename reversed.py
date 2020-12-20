"""
REVERSED

--> Não confundir com a função reverse, que inverte a ordem de listas.

--> Funciona com qualquer iterável.

--> Sua função é inverter o iterável.

--> Retorna um iterável chamado List Reverse Iterator
"""

lista = [1,2,3,4,5]
res = reversed(lista)
print(lista)  # [1, 2, 3, 4, 5]

print(res)  # <list_reverseiterator object at 0x000002854DA00E20>

print(type(res))  # <class 'list_reverseiterator'>

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

print(list(reversed(lista)))  # [5, 4, 3, 2, 1]

print(tuple(reversed(lista)))  # (5, 4, 3, 2, 1)

print(set(reversed(lista)))  # {1, 2, 3, 4, 5}
# Em conjuntos (sets), não definimos a ordem dos elementos.

# Iterando sobre o reversed:

for letra in reversed('Geek University'):
    print(letra, end='')  # ytisrevinU keeG
print('\n')
print(''.join(list(reversed('Geek University'))))  # ytisrevinU keeG

print('Geek University'[::-1])  # ytisrevinU keeG

# Podemos também usar o reversed para fazer um loop for reverso:

for n in reversed(range(0,10)):
    print(n)

# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

for n in range(9, -1, -1):
    print(n)
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0