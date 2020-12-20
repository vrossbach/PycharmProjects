"""
Métodos de data e hora

agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# DIFERENÇA: com now() podemos especificar o timezone

# Mudanças ocorrendo à meia-noite --> combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# O último parâmetro zera o relógio para fazer a manutenção à meia-noite.

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana --> weekday()

# Os dias da semana do método weekday() começam em zero, sendo o zero igual à segunda-feira
# 0 - monday
# 1 - tuesday
# 2 - wednesday
# 3 - thursday
# 4 - friday
# 5 - saturday
# 6 - sunday

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
else:
    print('Você nasceu em um domingo')

# Formatando data/hora com strftime (string format time)

hoje = datetime.datetime.today()
hoje_formatado = hoje.strftime('%d/%m/%Y')
# print(hoje_formatado)
hoje_formatado = hoje.strftime('%d de %B de %Y')
# print(hoje_formatado)

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    if data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    if data.month == 3:
        return f'{data.day} de Março de {data.year}'
    if data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    if data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    if data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    if data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    if data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    if data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    if data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    if data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    if data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

print(formata_data(hoje))

import datetime
from textblob import TextBlob
# TextBlob é usado no processamento de linguagem natural

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"
# Método é demorado

hoje = datetime.datetime.today()

print(formata_data(hoje))

import datetime

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora:

almoco = datetime.time(12, 30, 0)
print(almoco)


"""


# Marcando tempo de execução do nosso código com timeit:

import timeit, functools

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

# Forma de testar a performance da função:
print(timeit.timeit(functools.partial(teste, 2), number=10000))

