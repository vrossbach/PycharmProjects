"""
Recebendo dados do usuário
Todo dado recebido pelo input é do tipo string
String => tudo o que estiver entre aspas simples, duplas ou triplas
ou seja: '', "", ''' ''', """ """
"""
# Entrada de dados
# print('Qual seu nome?')
# nome = input()  # Entrada de dir(__builtins__)

nome = input('Qual seu nome?')

# Exemplo de print do Python 2.x:
# print('Seja bem-vindo(a)%s' % nome)

# Exemplo de print do Python 3:
# print('Seja bem-vindo(a) {0}'.format(nome))

# Forma mais atual de print a partir do 3.7:
print(f'Seja bem-vindo {nome}')
# print('Qual sua idade?')
# idade = input()
idade = int(input('Qual sua idade?'))

# Processamento

# Saida de dados
# Exemplo de print do Python 2.x:
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print do Python 3:
# print('A {0} tem {1} anos.'.format(nome, idade))

print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2020 - idade}')  # int(idade)  => cast
# cast é a conversão de um tipo de dado em outro
