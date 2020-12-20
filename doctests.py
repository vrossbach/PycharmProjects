"""
DOCTESTS

--> O próprio teste serve como documentação

--> Lembrar das docstrings: doctests são testes colocados na docstring

--> Criamos documentações que funcionam como testes

Para rodar um doctest:

python -m doctest -v nome_do_modulo.py

def soma(a, b):
    # soma os números a e b

#     soma(1, 2)
    #3
#     soma(2, 4)
  #  6
    #
  #  return a + b
Saída do terminal:
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Aplicando TDD:

def duplicar(valores):
    #duplica os valores em uma lista
#    >>>duplicar([1, 2, 3, 4])
#    [2, 4, 6, 8]
#    >>>duplicar([])
#    []
#    >>>duplicar(['a', 'b', 'c'])
#    ['aa', 'bb', 'cc']
#    >>>duplicar([True, None])
#    Traceback (most recent call last):
#      ...
#    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
#    return [2 * elemento for elemento in valores]

"""

# Erro inesperado
def fala_oi():
    """Fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"
# Dentro do doctest o Python não reconhece aspas duplas, devem ser simples

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
# Se colocar espaços depois de True e usar editor de texto comum, o teste falha.


