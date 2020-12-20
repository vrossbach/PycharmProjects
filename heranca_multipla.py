#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO - HERANÇA MÚLTIPLA

--> Herança múltipla nada mais é do que a possibilidade de
    uma classe herdar de múltiplas classes, fazendo com
    que a classe filha herde todos os atributos e métodos
    das classes herdadas.

--> A herança múltipla pode ser feita de duas maneiras:
    --> Por multiderivação direta;
    --> Por multiderivação indireta.
"""

# Multiderivação direta

class Base1:
    pass

class Base2:
    pass

class Multiderivada(Base1, Base2):
    pass

# Multiderivação indireta:

class Base3:
    pass

class Base4(Base3):
    pass

class Base5(Base4):
    pass

class Multiderivada2(Base5):
    pass

""" Não importa se a derivação é direta ou indireta.
A classe que realizar a herança herdará todos os 
atributos e métodos da super classe. """

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Eu sou o {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nada(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} do mar'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def anda(self):
        return f'{self._Animal__nome} está andando'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

baleia = Aquatico('Wally')
print(baleia.nada())
print(baleia.cumprimenta())

tatu = Terrestre('Xim')
print(tatu.anda())
print(tatu.cumprimenta())

tux = Pinguim('Tux')
print(tux.anda())
print(tux.nada())
print(tux.cumprimenta())  # da terra (Method Resolution Order - MRO

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')

print(f'Tux é instância de Aquático? {isinstance(tux, Aquatico)}')

print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')

print(f'Tux é instância de object? {isinstance(tux, object)}')

print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')

# Todos são True