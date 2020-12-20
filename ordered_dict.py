"""
ORDERED DICT (MÓDULO COLLECTIONS)

--> Nos dicionários a ordem de inserção dos elementos não é garantida.

dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(dicionario)

for chave,valor in dicionario.items():
    print(f"chave={chave}:valor = {valor}")

OrderedDict é um dicionário que nos garante retornar a ordem de inserção dos elementos.
# Fazendo o import:
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave,valor in dicionario.items():
    print(f"chave={chave}:valor = {valor}")
    # chave=a:valor = 1
    # chave=b:valor = 2
    # chave=c:valor = 3
    # chave=d:valor = 4
    # chave=e:valor = 5
"""

# DIFERENÇAS ENTRE DICT E ORDERED DICT:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True (a ordem dos elementos não importa em DICT)

# ORDERED DICT:
from collections import OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False (a ordem de inserção é diferente)
