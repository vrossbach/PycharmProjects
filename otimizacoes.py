import collections
from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))
# Tempo necessário para encontrar o atributo diminuiu
# 0.035305100000000006

import sys
print(sys.getsizeof(list(range(29082020))))
# melhoria no gerenciamento de memória

# python.org/downloads - active python releases (para consultar otimizações)

