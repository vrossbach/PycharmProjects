"""

ENTENDENDO O *args

--> O *args é um parâmetro como outro qualquer de entrada de uma função.
    Isso significa que você pode chamar de qualquer coisa, desde que comece com *

EXEMPLO:
*xis

--> Por convenção utilizamos *args para defini-lo

--> O parâmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tuplo,
    então desde já lembre-se de que tuplas são imutáveis

# Exemplo

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))

# Se informarmos mais ou menos do que 3 parâmetros, teremos TypeError

"""


# ENTENDENDO O *args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2, 3))


# ou

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2, 3))


# Para que a soma funcione o valor informado deve ser INTEIRO ou REAL.

# EXEMPLO:

def soma_todos(nome, email, *args):
    return sum(args)


print(soma_todos('Angelina', 'Jolie'))

# EXEMPLO:

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Quem é você?'

print(verifica_info())
print(verifica_info(1,True,'University','Geek'))
print(verifica_info('University',3.145))

def soma_todos_numeros(*args):
    print(args)  # Cria uma tupla com a lista dentro, considerando a lista como um único elemento
    return sum(args)
print(soma_todos_numeros())
print(soma_todos_numeros(1,4,5,6))
numeros = [1,2,3,4,5,6,7]
#  print(soma_todos_numeros(numeros))  # TypeError

# SOLUÇÃO: desempacotar a lista:
num1, num2, num3, num4, num5, num6, num7 = numeros

print(soma_todos_numeros(*numeros))
# OBS.: o asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisa antes desempacotar estes dados.
# Coleção pode ser lista, tupla, conjunto (set)... mas não dict