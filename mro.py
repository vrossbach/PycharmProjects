#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO  - Method Resolution Orden (MRO)

MRO  é a ordem de execução dos métodos (quem será executado primeiro).

Em Python, podemos conferir a ordem de execução dos métodos
de 3 formas:
--> via propriedade da classe __mro__
--> via método mro()
--> via help

A ordem de execução depende do que foi informado primeiro:

class Pinguim(Terrestre, Aquatico):

ou

class Pinguim(Aquatico, Terrestre):
"""

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

tux = Pinguim('Tux')
print(tux.cumprimenta())  # da terra (Method Resolution Order - MRO
