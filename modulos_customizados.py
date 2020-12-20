"""
MÓDULOS CUSTOMIZADOS

--> Como m[odulos Python nada mais são do que arquivos Python,
    então todos os arquivos que criamos neste curso são módulos Python
    prontos para serem utilizados.
"""

from funcoes_com_parametro import soma_impares

print(soma_impares([1,2,3,4,5,6,7,8,9]))

# Um módulo não deve ter execução de código dentro dele (ex.: print()) pois
# tudo isso será impresso junto com a função importada

"""
Se importarmos todo o módulo, teremos acesso a todos os elementos
dele. Por exemplo, se houver uma lista dentro dele teremos acesso a ela.
"""

import funcoes_com_parametro as fcp

print(fcp.lista)  # [1, 2, 3, 4, 5, 6, 7]

print(fcp.tupla)  # (1, 2, 3, 4, 5, 6, 7)

print(fcp.soma_impares(fcp.lista))  # 16

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))