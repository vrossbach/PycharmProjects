"""
FUNÇÕES COM RETORNO

numeros = [1,2,3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)  # [1, 2]
print(f'Retorno de pop: {ret_pr}')  # None

OBS.: Em Python, quando uma função não retorna nenhum valor
      o retorno é None

--> Funções Python que retornam valores devem retorná-los com a palavra reservada 'return'

--> Não precisamos necessariamento criar uma variável para receber o retorno da funaçõ.
    Podemos passar a execução da função para outras funções como o print().
"""


# Exemplo 1

# def quadrado_de_7():
#     print(7*7)

# ret = quadrado_de_7()  # 49
# print(f'Retorno {ret}')  # None

# Refatorar a função para que ela retorne o valor:

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno {ret}')  # Retorno 49

print(f'Retorno: {quadrado_de_7()}')  # Retorno: 49


# Refatorando a primeira função:

def diz_oi():
    return 'Oi'


print(diz_oi())  # Oi

alguem = 'Pedro'

print(f'{diz_oi()}, {alguem}!')

"""
RETURN:
--> finaliza a função, ou seja, sai da execução da função
--> podemos ter em uma função diferentes returns
--> se houver múltiplos returns, somente um deles será executado
--> podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores

"""


# EXEMPLO 1:

def diz_oi():
    print('Estou sendo executado antes do retorno')  # imprime
    return 'Oi!'
    print('Estou sendo executado após o retorno')  # não imprime


print(diz_oi())


# Após o retorno, nada é executado

# EXEMPLO 2:

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())  # 4 se True, 3.2 se None, b se False

# EXEMPLO 3:

def outra_funcao():
    return 2,3,4,5

num1, num2, num3, num4 = outra_funcao()  # desempacotar tupla
print(num1, num2, num3, num4)

# ou:

print(outra_funcao())  # imprime como tupla
print(type(outra_funcao()))  # <class 'tuple'>

# Vamos criar uma função para jogar a moeda (cara ou coroa):

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Pseudo-randômica é quando gera repetição

# ---------------------
# from funcoes_com_retorno import joga_moeda

#  ERROS COMUNS NA UTILIZAÇÃO DO RETORNO, MAS QUE NA VERDADE SÃO CODIFICAÇÕES DESNECESSÁRIAS:

def eh_impar():
    numero = 5
    if numero % 2 != 0:  # % é sobra da divisão
        return True
    else:  # linha de código desnecessária
        return False

print(eh_impar())