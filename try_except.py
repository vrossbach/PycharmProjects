"""
BLOCK TRY/EXCEPT

--> Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso
    código, prevenindo assim que o programa pare de funcionar e o
    usuário receba mensagens de erro inesperadas.
--> A forma geral mais simples é:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas
"""

# Tratando um erro genérico (qualquer tipo:
try:
    geek()  #NameError
except:
    print('Deu algum problema')
""" Tente executar a função geek(). Caso você encontre erros,
imprima a mensagem de erro."""

try:
    len(5)
except:
    print('Deu algum problema')

""" Tratar um erro de forma genérica não é a melhor forma de 
tratamento de erros. O ideal é sempre tratar de forma específica."""

# Tratando um erro específico:

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

try:
    len(5)
except TypeError:
    print('O tipo de dado está incorreto')

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
    # A aplicação gerou o seguinte erro: object of type 'int' has no len()

# Podemos efetuar diversos tratamentos de erro ao mesmo tempo:
try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

# ----------------------------------------------------------------
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": 'Geek'}

print(pega_valor(dic, "game"))  # KeyError

print(pega_valor(7, "nome"))  # TypeError

print(pega_valor(dic, "8"))  # TypeError


