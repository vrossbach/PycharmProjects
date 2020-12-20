#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
"""
PROGRAMAÇÃO ORIENTADA A OBJETOS - POO
--> é um paradigma de programação que utiliza o mapeamento de
    objetos do mundo real para modelos do mundo real.
--> Paradigma: metodologia usada para pensar/desenvolver sistemas

Principais elementos:
classe --> modelo do objeto do mundoo real sendo representado computacionalmente
atributo --> características do objeto
método --> comportamento do objeto (funções)
construtor --> método especial usado para criar os objetos
objeto --> instância da classe

--> Quando criamos nossas classes estamos definindo nossos
    próprios tipos de dados


Paradigmas:

Estruturado
--> linguagem C suporta
---------------------------------------------------------
Orientação a objeto
--> linguagem C não suporta
--> 95% do que vimos até aqui foi estruturado
--> mapear (modelar) objetos do mundo real

Elementos
--> classe (molde)
    --> atributos (características do objeto)
--> objetos/instâncias: elementos criados com base na classe
--> construtor: método especial para criar objetos a partir da classe

--------------------------------------------------------
Funcional

Python é multiparadigma (suporta os 3 paradigmas)


"""
numero = 10
print(numero)
print(type(numero))
# 10
# <class 'int'>

nome = 'Geek'
print(nome)
print(type(nome))
# Geek
# <class 'str'>

class Produto:
    pass

ps4 = Produto()  # --> método (construtor da classe produto)
print(ps4)
print(type(ps4))
# <__main__.Produto object at 0x000001D7041C5FD0>
# <class '__main__.Produto'>