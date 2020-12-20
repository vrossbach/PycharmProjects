"""
Módulo Collections - NAMED TUPLE

Recap TUPLA:
tupla = (1,2,3)
print(tupla[1])  # 2

#Named Tuple --> são tuplas diferenciadas onde especificamos um nome para a mesma e
também parâmetros.
"""

from collections import namedtuple

# Definir o nome e parâmetros:

# Forma 1: declaração Named Tuple
cachorro = namedtuple('cachorro','idade raca nome')

# Forma 2 - declaração
cachorro = namedtuple('cachorro','idade, raca, nome')

# Forma 3: declaração
cachorro = namedtuple('cachorro', ['idade','raca','nome'])

# ---------------------------------------------------------
ray = cachorro(idade=2,raca='chow-chow',nome='Ray')
print(ray)
# cachorro(idade=2, raca='chow-chow', nome='Ray')

# Acessando os dados:

print(ray[0]) # idade
print(ray[1]) # nome
print(ray[2]) # raça

print(ray.idade)
print(ray.nome)
print(ray.raca)

print(ray.index('chow-chow')) # 1
print(ray.count('chow-chow')) # quantas ocorrências