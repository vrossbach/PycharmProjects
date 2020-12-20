#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
FUNÇÕES DE MAIOR GRANDEZA (Higher Order Functions - HOF)

--> Quando uma linguagem de programação suporta HOF, isso
    indica que podemos ter funções que retornam outras
    funções como resultado ou mesmo que podemos passar
    funções como argumento para outras funções, e até mesmo
    criar variáveis do tipo funções para os nossos programas.

--> O conceito de HOF já foi usado na seção de funções.

"""


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções:

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

"""
--> Em Python, as funções são cidadãos de primeira classe
(first class citizen)
"""

"""
NESTED FUNCTIONS --> funções aninhadas
--> Em Python, podemos também ter funções dentro de 
    funções, que são conehcidas por Nested Functions ou
    Inner Functions (funções internas)
"""

from random import choice  # choice seleciona aleatoriamente


def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))

    return humor() + pessoa


print(cumprimento('Angelina'))
print(cumprimento('Felicia'))

"""
Retornando funções de outras funções:
"""


def faz_me_rir():
    def rir():
        return choice(('kkk', 'hahaha', 'jajaja'))

    return rir()


rindo = faz_me_rir()
print(rindo)

"""
Inner functions / Nested functions podem acessar o escopo
de funções mais externas.
Exemplo: humor acessa pessoa
"""


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkk', 'hahaha', 'jajaja'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
