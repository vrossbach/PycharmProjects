#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO - MÉTODOS MÁGICOS

--> São todos os métodos que utilizam dunder (__)

dunder init --> __init__()

dunder --> double underscore

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# Representação do objeto: __repr__
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)
# <__main__.Livro object at 0x000001FEF6DC5FD0>
# <__main__.Livro object at 0x000001FEF6DC5F10>
# Endereços de memória onde os objetos estão armazenados

print(str(livro1))  # <__main__.Livro object at 0x0000024D84435FD0>

# Python Rocks! escrito por Geek University
# Inteligência Artificial com Python escrito por Geek University
# Python Rocks! escrito por Geek University

# OBS.: se houver 2 returns só retorna o primeiro porque o return finaliza o método

"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# Representação do objeto:
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

# String é executado no lugar de repr, não importa a ordem em que aparecem
    def __str__(self):
        return self.titulo

# __len__ sozinho não existe, precisa ser especificado qual self retornar
    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória.')

    def __add__(self, outro):
        return f'{self} + {outro}'  # se colocar sinal de menos vai concatenar com -

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg+= ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)

# Forçando a execução do repr:
print(repr(livro1))
# Python Rocks! escrito por Geek University

print(len(livro1))  # 400

print(livro1 + livro2)

# Inteligência Artificial com Python
# Python Rocks! escrito por Geek University
# 400
# Python Rocks! + Inteligência Artificial com Python
# Um objeto do tipo Livro foi deletado da memória.
# Um objeto do tipo Livro foi deletado da memória.

# Quando os objetos são executados eles são deletados da memória
# e por isso aparece a mensagem.

print(livro1 * 3)  # retorno do __mul__

# OS MÉTODOS DUNDER TESTADOS SÃO EXEMPLOS DE POLIMORFISMO