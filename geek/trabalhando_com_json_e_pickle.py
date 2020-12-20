"""
JSON e Pickle

JSON --> JavaScript Object Notation

--> Usados em API's (Google, Facebook, etc.)

API --> meios de comunicação entre os serviços oferecidos
        por empresas (Twitter, Facebook, etc.) e terceiros
        (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'Playstation 4':('2 TB', 'Novo', '220 V', 2340)}])

print(type(ret))

print(ret)
# <class 'str'>
# ["produto", {"Playstation 4": ["2 TB", "Novo", "220 V", 2340]}]
# JSON só trabalha com aspas duplas

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'siames')

# print(felix.__dict__)

# ret = json.dumps(felix.__dict__)

# print(ret)

ret = jsonpickle.encode(felix)
print(ret)
# {"py/object": "__main__.Gato", "_Gato__nome": "Felix", "_Gato__raca": "siames"}

# Integrando o JSON com Pickle: pip install jsonpickle

 ESCREVENDO O ARQUIVO json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'siames')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

"""

# LENDO O ARQUIVO json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'siames')

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

# <__main__.Gato object at 0x000001C0F2E41DF0>
# <class '__main__.Gato'>
# Felix
# siames