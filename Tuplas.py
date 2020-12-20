"""
TUPLAS (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses.

2 - As tuplas são imutáveis, ou seja, ao se criar uma tupla ela não muda.
    Toda operação em uma tupla gera uma nova tupla.
    Os comandos sort, append e shallow copy não modificam uma tupla.

# CUIDADO:
    - as tuplas são representadas por parênteses, mas podem ser criadas sem parênteses:
tupla1 = (1,2,3,4,5,6)
print(type(tupla1))
print(tupla1)

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

    - tuplas com 1 elemento:
tupla3 = (4)  # isto não é uma tupla, mas sim um inteiro
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # isto é uma tupla
print(tupla4)
print(type(tupla4))

tupla4 = 5,  # isto é uma tupla
print(tupla5)
print(type(tupla5))

***Tuplas são definidas pela separação dos elementos por VÍRGULA, e não pero parênteses.

# Gerar tuplas dinamicamente com ranges(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Desempacotamento de tupla:
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)  # Geek University
print(curso)  # Programação em Python: Essencial
# Gera erro se colocarmos um número diferente de elementos para desempacotar.
# Métodos para adição e remoção de elementos nas tuplas não existem,
# dado o fato de as tuplas serem imutáveis

# SOMA, VALOR MÁXIMO E MÍNIMO, TAMANHO
# Se os valores forem todos inteiros ou reais, é possível fazer soma, máx e mín
tupla = 1,2,3,4,5,6
print(sum(tupla))  # 21
print(max(tupla))  # 6
print(min(tupla))  # 1
print(len(tupla))  # 6

# CONCATENAÇÃO DE TUPLAS (juntar tuplas)
# - As tuplas originais não se alteram
tupla1 = 1,2,3
print(tupla1)
tupla2 = 4,5,6
print(tupla2)
print(tupla1+tupla2)  # (1, 2, 3, 4, 5, 6)
print(tupla1)  # (1, 2, 3)
print(tupla2)  # (4, 5, 6)

# Tuplas são imutáveis mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla 2 # sobrescreve a tupla 1

# Verificar se determinado elemento está contido na tupla
tupla = 1,2,3
print(3 in tupla) # imprime True se o número 3 está na tupla

# ITERANDO SOBRE UMA TUPLA
tupla = 1,2,3
for n in tupla:
    print(n) # imprime tudo
for indice, valor in enumerate(tupla):
    print(indice, valor)
    # 0 1
    # 1 2
    # 2 3

    # Contando elementos dentro de uma tupla:
tupla = ('a','b','c,','d','e','a')
print(tupla.count('a'))  # 2

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))
# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')
# 3
# Converte en string e conta quantas letras 'e' existem

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# O acesso a elementos em uma tupla é semelhante ao de uma lista (via índice)
tupla = 1, 2, 3, 4, 5, 6
print(tupla[5])

i = 0
while i < len(tupla):
    print(tupla[i])
    i = i + 1

print(tupla(index[1]))

# slicing
# tupla[inicio:fim:passo]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla[0::])

# Por que utilizar tuplas?
--> são mais rápidas do que listas para operações
--> deixam o código mais seguro (imutável)

# COPIAR UMA TUPLA PARA OUTRA (na lista gera shallow copy mas na tupla, não)
tupla = (1,2,3)
nova = tupla
print(nova)
print(tupla)
outra = (4,5,6)
nova = nova + outra
print(nova)  # (1,2,3,4,5,6)
print(tupla)  # (1,2,3)
"""



