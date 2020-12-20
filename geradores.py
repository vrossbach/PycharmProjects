#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
"""
GERADORES

--> São os generators
--> São iterators (iteradores)
--> Nem todo iterator é um generator
--> Generators podem ser criados com funções geradoras
    que usam a palavra reservada yield
--> podem ser criados com expressões geradoras

DIFERENÇAS ENTRE FUNÇÕES E GENERATOR FUNCTIONS

----------------------------------------------------------------
Funções                       Generator functions
----------------------------------------------------------------
- utilizam return             - utilizam yield
- retornam 1 vez              - pode usar yield múltiplas vezes
- quando executada, retorna   - quando executada, retorna um
  um valor                      generator
----------------------------------------------------------------
"""

# Exemplo de generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# quando aplicamos return saímos de dentro da função
# yield retorna o valor e aguarda uma função next()

"""
Uma generator function não é um generator;
ela GERA um generator


gen = conta_ate(5)
# print(type(gen))
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5

"""
gen = conta_ate(10)

print(next(gen))

print('Geek')

for num in gen:
    print(num)  # imprime de 1 a 10

# Para gerar todos de 1 vez: gen = list(conta_ate(10))

