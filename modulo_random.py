"""
MÓDULO RANDOM

--> O que são módulos?
    --> Em Python, módulos nada mais são do que outros arquivos Python.
    --> Se temos um arquivo com uma função, podemos importar a função deste
        arquivo e usá-la em outro arquivo.
    --> Os programadores compartilham seus códigos no formato de pacotes.

--> Módulo random

    --> para utilizar o módulo, devemos instalá-lo ou importá-lo.
    --> O módulo random precisa ser importado, pois é integrado e está pronto para uso.
    --> O módulo random possui várias funções para geração de números pseudo-aleatórios.

--> Existem 2 formas de se utilizar um módulo ou função deste:

import random

    --> ao realizar o import de todo o módulo, todas as funções, atributos,
        classes e propriedades que estiverem dentro do módulo ficarão disponíveis
        (ficarão em memória) -- não recomendado. Caso você saiba quais funções deste
        módulo precisa utilizar, é melhor importar somente estas funções.


"""

# import random

# print(random.random())  # 0.18998397116704613

# random() gera um número pseudoaleatório entre 0 e 1

# para utilizar a função random() do pactore random, nós colocamos o nome
# do pacote e o nome da função separados por ponto.

# Não confundir a função random() com o pacote random. Pode parecer confuso,
# mas a função random() é apenas uma das funções dentro do módulo random

# -------------------------------------------------------------
from random import random  # Forma recomendada

""" 
No import acima, estamos importando somente uma função do módulo random
"""

for i in range(10):
    print(random())  # gera 10 números entre 0 e 1

# A FUNÇÃO ACIMA É USADA EM REDES NEURAIS (pesos)
# Os pesos são inicializados com random()

"""
A função uniform() gera números pseudo-aleatórios entre os valores
estabelecidos
"""
print('\n')

from random import uniform

for i in range(10):  # gera 10 números entre os limites dados
    print(uniform(3, 7))  # o 7 não é incluído

print('\n')

"""
A função randint() gera números pseudo-aleatórios inteiros entre os 
limites informados
"""

# Gerador de apostas para a mega-sena

from random import randint

for i in range(6): #  gera 6 números ( 0 a 5)
    print(randint(1, 61), end=', ')  # 61 não é incluído
"""
choice() --> mostra um valor aleatório entre um iterável.
"""
print('\n')
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

print(choice('Geek University'))  # seleciona uma letra da string

"""
shuffle() --> embaralha os dados
"""

print('\n')

from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas[0])  # tira a certa que o usuário pegou do baralho
