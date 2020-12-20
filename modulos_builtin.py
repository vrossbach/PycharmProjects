"""
MÓDULOS BUILT-IN
Global Module Index em docs.python.org

--> São módulos integrados que, por padrão, já vêm instalados na linguagem Python.

________________________
|Python|Módulos builtin|
------------------------


--> Os módulos são instalados mas não são carregados junto com a linguagem cada
    vez que abrimos um novo arquivo.
"""

# Utilizando alias (apelidos) para módulos/funções

import random as rdm  # rdm é o alias de random

print(rdm.random())

# Podemos importar todas as funções de um módulo usando o asterisco

from random import *

print(random())  # desta forma não precisa usar random.random()

# Podemos também dar um alias para uma função:

from random import randint as rdi

print(rdi(5, 89))

# Fazendo vários imports de um único módulo:

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(randint(3, 7))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

