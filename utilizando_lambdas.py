"""
UTILIZANDO LAMBDAS

Conhecidas cpor Expressões Lambdas ou simplesmente Lambdas,
são funções sem nome, ou seja, funções anônimas.

# Função em Python

def soma(a, b):
    return a + b

"""
# Exemplo de função em Python:
def funcao(x):
    return 3 * x + 1


print(funcao(4))  # 13
print(funcao(7))  # 22

# Exemplo de expressão lambda:

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(4))  # 13
print(calc(7))  # 22

# Podemos ter expressões lambdas com múltiplas entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip() remove os espaços no início e no fim da variável.

print(nome_completo(' angelina ', 'JOLIE'))  # Angelina Jolie
print(nome_completo('  FELICITY ', 'jones'))  # Felicity Jones

# Em funções Python, podemos ter nenhuma ou várias entradas.
# Em lambdas isso também é possível.

amar = lambda : 'Como não amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ... xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Como não amar Python?
# 19
# 5.916079783099616
# 4.909090909090908

# OBS.: Se passarmos mais ou menos argumentos do que parâmetros esperados,
# teremos TypeError

autores = ['Isaac Asimov', 'Ray Bradbury', 'Jorge Amado', 'Oscar Wilde', 'Virginia Woolf', 'Ligia Fagundes Teles',
           'H. G. Weels']
print(autores)

# Modo como LAMBDA normalmente é usado:
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# split(' ') transforma o nome completo em uma lista com palavras
# [-1] pega o último elemento
# lower() transforma tudo em minúscula


print(autores)
# ['Jorge Amado', 'Isaac Asimov', 'Ray Bradbury', 'Ligia Fagundes Teles', 'H. G. Weels', 'Oscar Wilde', 'Virginia Woolf']

# Função quadrática:

# f(x) = a * x ** 2 + b * x + c

# Definindo a função:

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função quadrática f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# -5
# 0
# 9

print(geradora_funcao_quadratica(2, 3, -5)(2))  # 9

# LAMBDAS são usados para fazer filtragem e ordenação de dados, dentre outras aplicações.

