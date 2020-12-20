"""
Listas

Listas em Python funcionam como vetores ou matrizes (arrays) com a diferença de serem DINÂMICOS e também de podermos
colocar QUALQUER tipo de dado.

Linguagens C/Java: arrays
- Possuem tamanho e tipo de dado fixos; ou seja, nestas linguagens, se você criar um array do tipo int e com tamanho 5
(guardar até 5 valores), este array será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python,
- Dinâmico: não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
- A lista não é infinita; enquanto houver memória disponível na máquina, você pode adicionar elementos.
- As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.
- As listas em Python são representadas por colchetes []

type([])
lista1 = [1, 99, 4, 27, 15, 2, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')  # O mesmo que a lista 2

# Podemos facilmente checar se determinado valor está contido na lista:
num = 18
if {num} in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))  # quantos números 1 há na lista 1
print(lista5.count('e'))  # quantas letras 'e' há na lista 5 (usado em sequência de DNA)

# Adicionar elementos em listas

# Para adicionar elementos ou valores em listas, utilizamos a função
append

print(lista1)
lista1.append(42)
print(lista1)

# Obs.: com 'append' só conseguimos adicionar 1 elemento por vez.

lista1.append([8, 3, 1])  # Coloca a lista como sublista
print(lista1)
# Neste caso não foi adicionado mais de um elemento, mas sim um único elemento do tipo lista []
# A saída fica: [1, 1, 2, 3, 4, 15, 27, 27, 42, 44, 99, 42, [8, 3, 1]]
# Ou seja, uma lista dentro de outra lista

if [22, 27, 27] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')
# Só é possível verificar a presença de 1 elemento por vez na lista

lista1.extend([123, 44, 67])  # Coloca cada elemento avulso na lista como valor adicional
print(lista1)
# Saída: [1, 1, 2, 3, 4, 15, 27, 27, 42, 44, 99, 42, [8, 3, 1], 123, 44, 67]
# Extend não aceita valor único; para valor único usa-se append
# Extend só aceita iteráveis

# O valor inserido como append vai sempre para o final da lista
# Extend também coloca os valores no final da lista
# Podemos inserir um novo elemento na lista informando a posição do índice para que não fique no final
lista1.insert(2, 'Novo Valor')  # insere novo valor na posição 2 sem substituir o valor inicial
                                #  que é deslocado para a direita

# Podemos facilmente juntar 2 listas:
# lista6 = lista1 + lista2
ou
lista1.extend(lista2)
print(lista1)

# Podemos inverter uma lista usando o reverse:
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

# outro modo de inverter a lista:
print(lista1[::-1])
print(lista2[::-1])

#Copiar uma lista:
lista6 = lista2.copy()
print(lista6)

# Contar quantos elementos existem dentro da lista
print(len(lista1))

# Remover o último elemento da lista:
print(lista5)
lista5.pop()
print(lista5)
# O pop() remove o último elemento e retorna qual elemento removeu

# Remover um elemento pelo seu índice:
lista5.pop(2)
print(lista5)
# Os elementos à direita deste índice serão deslocados para a esquerda
# Se não houver elemento no índice informado, temos o erro index error

# Remover todos os elementos da lista:
print(lista5)
lista5.clear()
print(lista5)

#Repetir elementos em uma lista:
nova = [1,2,3]
print(nova)
nova = nova*3
print(nova)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#  Converter uma string para uma lista:

#  Exemplo1
curso = 'Programação em Python Essencial'
print(curso)
curso=curso.split()
print(curso) # ['Programação', 'em', 'Python', 'Essencial']
# Por padrão, o split separa os elementos da lista pelo espaço entre eles

#  Exemplo 2
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso) #  ['Programação', 'em', 'Python', 'Essencial']

#  Converter lista em string:
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)
curso = ' '.join(lista6)
#  Este comando pega a lista 6, coloca espaços entre os elementos e forma uma string
print(curso)  # Programação em Python Essencial

curso = '$'.join(lista6)
#  Este comando coloca $ entre cada elemento da lista e a transforma em uma string
print(curso)  # Programação$em$Python$Essencial

lista6 = [1,2.34,True,'Geek', 'd', [1,2,3], 453575467]
print(lista6)
print(type(lista6))
# [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 453575467]
# <class 'list'>

#  Iterar sobre uma lista:

#  Exemplo 1 - utilizando for
soma = 0
for elemento in lista1:
    print(elemento) #  Imprime todos os elementos da lista 1
    soma= soma + elemento
print(soma)  # Resultado da soma dos elementos da lista

#  Exemplo 2 - utilizando while
carrinho =[]
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

    #  Utilizar variáveis em listas:
numeros = [1,2,3,4,5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#  Em listas, fazemos acesso aos elementos de forma indexada.

cores = ['verde', 'amarelo', 'azul', 'branco']
#         pos0      pos1      pos2     pos3

print(cores[0])  # verde
print(cores[1])  # amarelo

#  Acesso de forma indexada inversa:
print(cores[-1])  # branco
print(cores[-2])  # azul

# só aceita neste caso -1, -2, -3 e -4

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

    # Se for necessário criar o índice:
# Gerar índice em um for:
for indice, cor in enumerate(cores):
    print(indice, cor)

    # Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Existem outros tipos de coleções que não aceitam repetição.

# OUTROS MÉTODOS

# Encontrar o índice de um elemento na lista:
numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(6))  # Em qual índice está o valor 6
# Caso não tenha este elemento na lista, será apresentado erro

print(numeros.index(5))  # retorna o índice do primeiro 5 da lista

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # procurar o índice do valor 5 a partir do índice 1
# Senão encontrar o elemento na lista, gera erro.

# Busca dentro de um range, inicio/fim
print(numeros.index(8,3,6))  # Buscar o índice do valor 8 entre os índices 3 e 6

# slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# slicing de listas com o parâmetro início

lista = [1, 2, 3, 4]
print(lista[1:])  # inicia no índice 1 e vai até o final - [2, 3, 4]
print(lista[::])  # imprime tudo
print(lista[-1:])  # imprime somente o 4
print(lista[-3:])  # imprime [2,3,4]
print(lista[:2])  # [1, 2] (não inclui o índice 2)

# Lista com o parâmetro passo:
print(lista[1::2])  # começa no índice 1 e imprime de 2 em 2
# [2,4]
print(lista[::2])  # começa no índice 0 e vai até o final de 2 em 2
print(lista[1::-1]) # [2, 1]

# Inverter valores em uma lista:

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes) # ['University', 'Geek']

# ou

nomes.reverse()
print(nomes)

# SOMA, VALOR MÁXIMO OU MÍNIMO E TAMANHO DA LISTA

# Em soma e valor máximo ou mínimo, os valores devem ser inteiros ou reais
from typing import List

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar uma lista em tupla:

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))
# [1, 2, 3, 4, 5, 6]
# <class 'list'>
# (1, 2, 3, 4, 5, 6)
# <class 'tuple'>

# Desempacotamento de listas:

lista = [1,2,3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# 1
# 2
# 3
# O número de elementos desempacotados deve ser igual ao número de valores da lista

# Cópia de lista (shallow copy e deep copy)

# Forma 1 - Deep copy

lista = [1,2,3]
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
# As modificações na nova lista não afetam a lista anterior (DEEP COPY - cópia profunda)

"""

# Forma 2 - Shallow copy

lista = [1,2,3]
print(lista)
nova = lista # cópia
nova.append(4)
print(lista)
print(nova)
# As modificações na cópia afetam a lista anterior (cópia via atribuição)
