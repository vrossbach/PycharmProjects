#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
FORÇANDO TIPOS DE DADOS COM DECORADORES

a = (1,2,3)
b = (4,5,6)
c = zip(a,b)
(1,2), (3,4), (5,6) 

"""

numero = 10

nome = 'Felicia'

"""
Em Java:
int numero = 10:
string nome = 'Felicia'
"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Geek', '3')
# Geek
# Geek
# Geek

@forca_tipo(float, float)
def dividir(a,b):
    print(a/b)

dividir('1', 5)  # 0.2