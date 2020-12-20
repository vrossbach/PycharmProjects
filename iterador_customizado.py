#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
"""
ESCREVENDO UM ITERADOR CUSTOMIZADO

range()
"""

# Revisão
for n in range(11):
    print(n)

"""
Precisamos usar algumas coisas que ainda não estudamos,
como orientação a objetos.

class --> método
__init__ --> construtor que cria os objetos a partir da classe
menor e maior --> parâmetros de entrada
self --> parâmetro de entrada padrão que representa o próprio objeto
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)  # imprime de 1 a 60

# O método anterior replicou a função range():
for n in range(1,61):
    print(n)  # imprime de 1 a 60

"""
con = Contador(1, 61)

print(con)  # <__main__.Contador object at 0x0000023162C05FD0>
# print(list(con))  # imprime a lista de 1 a 61 e StopIteration
print(con.menor)  # 1
print(con.maior)  # 61

it = iter(con)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
"""
