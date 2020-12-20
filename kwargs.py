"""
ENTENDENDO O **kwargs

--> O nome pode ser qualquer um, desde que tenha **, mas por convenção
é chamado de **kwargs.

--> Este é só mais um parâmetro mas, diferente do *args, que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados e transforma
esses parâmetros extras em um dicionário.
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')

    # A cor favorita de Marcos é verde.
    # A cor favorita de Julia é amarelo.
    # A cor favorita de Fernanda é azul.
    # A cor favorita de Vanessa é branco.


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
# {'marcos': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}

# OBS.: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')


# A cor favorita de Geek é navy.

# Exemplo mais complexo:

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Não tenho certeza de quem você é...
# Você recebeu um cumprimento Pythônico Geek!
# Oi Geek!
# especial Geek!

""" Nas nossas funções, podemos ter NESTA ORDEM:
1 --> parâmetros obrigatórios
2 --> *args
3 --> parâmetros default (não obrigatórios)
4 --> **kwargs
"""


def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_função(8, 'Julia')
minha_função(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_função(34, 'Felipe', eu='Não', voce='Vai')
minha_função(19, 'Carla', 9, 4, 3, java=False, python=True)


# Julia tem 8 anos
# ()
# Casado
# {}
# Felicity tem 18 anos
# (4, 5, 3)
# Solteiro
# {}
# Felipe tem 34 anos
# ()
# Casado
# {'eu': 'Não', 'voce': 'Vai'}
# Carla tem 19 anos
# (9, 4, 3)
# Casado
# {'java': False, 'python': True}

# Entendendo por que é importante manter a ordem dos parâmetros:

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
# [1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}]

# Função com a ordem correta dos parâmetros:

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

"""
O asterisco pode ser usado também para desempacotamento no **kwargs:
"""

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome':'Jones'}
print(mostra_nomes(nome='Felicity',sobrenome='Jones'))
print(mostra_nomes(**nomes))  # DESEMPACOTAMENTO DO DICIONÁRIO

def soma_multiplos_numeros(a,b,c, **kwargs):
    print(a+b+c)

soma_multiplos_numeros(1,2,3)

lista = [1,2,3]
tupla = 1,2,3
conjunto = {1,2,3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario=dict(a=1, b=2, c=3, nome='Geek')
soma_multiplos_numeros(**dicionario)

# OBS.: os nomes da chave em um dicionario devem ser os mesmos dos paâmetros da função
# ou gera TypeError

soma_multiplos_numeros(**dicionario, lang='Python')
