"""
DOCUMENTANDO FUNÇÕES COM DOC STRINGS

---> A informação entre aspas duplas triplas que estamos escrevendo é uma doc string
--> Importante para que futuramente saibamos por que o código foi feito
daquela forma.

OBS.: Podemos ter acesso à documentação de uma função em Python usando a propriedade especial
__doc__
EXEMPLO: print(diz_oi.__doc__)

--> Podemos ainda fazer acesso à documentação com a função heplp
EXEMPLO: help(diz_oi)
"""

print(help(print))  # Documentação da função print

# EXEMPLO 1:

def diz_oi():
    """Uma função simples que retorna a string 'Oi!"""
    return 'Oi!'

print(diz_oi())
print(help(diz_oi()))

# exemplo 2
def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero'^potencia
    :param numero: base do expoente
    :param potencia: expoente (neste caso 2)
    :return: retorna numero^potencia
    """
    return numero ** potencia