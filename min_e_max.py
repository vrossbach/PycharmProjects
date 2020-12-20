"""
MIN e MAX

max() --> retorna o maior valor em um iterável ou o maior de 2 ou mais elementos.

"""

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129
# funciona com listas, tuplas, sets, dicionários

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # 129

print(max(3, 34))  # 34

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(f'Maior valor: {max(val1, val2)}')

print(max('a', 'ab', 'abc'))  # abc: Maior ou o que vem depois na ordem alfabética

print(max('Geek University'))  # y (último na ordem alfabética)

"""
min() --> retorna o menor valor em um iterável ou o menor de 2 ou mais elementos
"""

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 129
# funciona com listas, tuplas, sets, dicionários

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # 129

print(min(3, 34))  # 34

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(f'Menor valor: {min(val1, val2)}')

print(min('a', 'ab', 'abc'))  # abc: Maior ou o que vem depois na ordem alfabética

print(min('Geek University'))  # y (último na ordem alfabética)
# O menor valor é o ESPAÇO VAZIO

# Outros exemplos:

nomes = ['Ana', 'Bruna', 'Carla', 'Denise', 'Elena', 'Fernanda']
print(max(nomes))  # Fernanda
print(min(nomes))  # Ana

# Para ordenar pelo tamanho (número de caracteres):
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "Thunderstuck", "tocou": 3},
    {"titulo": "Tudo mudar", "tocou": 2},
    {"titulo": "Sweet Child O'mine", "tocou": 4},
    {"titulo": "Bohemian Raphsody", "tocou": 32},
    {"titulo": "Back in Black", "tocou": 100},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprimir somente o título da música mais e menos tocada.

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Como encontrar a música mais e menos tocada sem usar max, min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])