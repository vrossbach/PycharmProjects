"""
FUNÇÕES COM PARÃMETRO PADRÃO

(Default parameters)

--> Funções onde a passagem de parâmetro seja opcional.
"""

# Exemplo: na função print é opcional informar o parâmetro de entrada
print('Geek University')
print()


def quadrado(numero):
    return numero ** 2


print(quadrado(3))


# print(quadrado())  # TypeError, pois parâmetro é obrigatório

def exponencial(numero, potencia=2):  # quando um parâmetro recebe valor (=2), ele se torna opcional.
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva à potência informada


# Obs.: se o usuário passar somente um parâmetro, este será atribuído a 'numero' e
# será calculado o quadrado deste número
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parãmetro número
# e o segundo ao parâmetro potência.

# OBS.: em funções Python, os parâmetros com valores Default DEVEM
# sempre estar ao final da declaração.
# ERRO: def teste(num=2, potencia)

# Outros exemplos:
def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))


# print(soma(4))  --> TypeError
# print(soma())  --> TypeError

def mostra_info(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Ozzy'))


# Parâmetros com valor padrão permitem maior flexibilidade nas funções,
# evitam erros com parâmetros incorretos e permitem trabalhar com
# exemplos mais legíveis de código

# Quais tipos de dados podemos usar como default?
# Qualquer tipo de dado (números, strings, floats, booleanos, listads, tuplas, dicionários, funções, etc.)

# Exemplo de função como parâmetro:

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # global ( não faz parte do escopo de nenhuma variável


def diz_oi():
    instrutor = 'Python'  # variável local se sobrepõe à global
    return f'Oi {instrutor}'


print(diz_oi())


def diz_oi():
    prof = 'Geek'  # só é reconhecida dentro do bloco onde foi declarada
    return f'Olá {prof}'


print(diz_oi())
# print(prof)  --> NameError

# ATENÇÃO com variáveis globais
# Se puder, evite

total = 0

"""
def incremento():
    total = total + 1  # UnboundLocalError (a variável não foi inicializada)
    return total
print(incremento())
"""


def incremento():
    global total
    total = total + 1  # Usa a variável global
    return total


print(incremento())

# Podemos ter funções que são declaradas dentro de funções e também têm uma forma
# especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora()) # sempre vai dar 1 porque o contador global sempre começa em zero.

