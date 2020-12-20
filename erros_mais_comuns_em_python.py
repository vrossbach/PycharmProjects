"""
ERROS MAIS COMUNS EM PYTHON
--> Builtin Exceptions in docs.python.org

Traceback --> saída de erros

É importante prestar atenção e aprender a ler as saídas de erros geradas
pela execução do nosso código.

Erros mais comuns:

SyntaxError --> ocorre quando o Python encontra um erro de sintaxe, ou seja,
                você escreveu algo que o Python não reconhece como parte da linguagem.

"""


# def funcao:
#    print('Geek University')
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 16
#     def funcao:
#               ^
# SyntaxError: invalid syntax

# correto:
def funcao():
    print('Geek University')


# ---------------------------------
# None = 1 # usando palavra reservada como variável
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 28
#     None = 1
#     ^
# SyntaxError: cannot assign to None

# ---------------------------------
# return # palavra reservada que deve ser colocada dentro de função
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 35
#     return
#     ^
# SyntaxError: 'return' outside function

"""
NameError --> ocorre quando uma variável ou função não foi definida.

"""

# geek # variavel não foi definida antes de ser usada
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 35
#     return
#     ^
# SyntaxError: 'return' outside function

# geek() # função não foi definida antes de ser usada
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 53, in <module>
#     geek()
# NameError: name 'geek' is not defined

# a = 18
# if a < 10:
#    msg = 'é menor que 10'
# print(msg) # msg não vai existir pq a nunca é menor que 10
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 63, in <module>
#     print(msg)
# NameError: name 'msg' is not defined

# correto:
a = 18
msg = 'algo'  # fazer declaração antes do bloco if para resolver o problema
if a < 10:
    msg = 'é menor que 10'
print(msg)

"""
TypeError --> ocorre quando uma função/operação/ação é aplicada a um tipo errado.
"""

# print(len(5))
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 80, in <module>
#     print(len(5))
# TypeError: object of type 'int' has no len()

# print('Geek'+ [])
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 86, in <module>
#     print('Geek'+ [])
# TypeError: can only concatenate str (not "list") to str

print(len('Geek' + 'University'))  # 14

"""
IndexError --> ocorre quando tentamos acessar um elemento em uma lista 
ou outro tipo de dado indexado usando um índice inválido.

--> O dado é indexado quando se pode fazer acesso a ele via índice.
"""

lista = ['Geek']
print(lista[0])
print(lista[0][0])  # Geek G
# print(lista[2]) # não existe, a lista só tem o elemento [0]
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 101, in <module>
#     print(lista[2])
# IndexError: list index out of range

"""
ValueError --> ocorre quando uma função ou operação builtin recebe um argumento
                com tipo correto mas valor inapropriado.
"""

print(int('42'))  # 42

# print(int('Geek'))
# print(float('Geek'))
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 117, in <module>
#     print(int('Geek'))
# ValueError: invalid literal for int() with base 10: 'Geek'

"""
KeyError --> ocorre quando tentamos acessar um dicionário com uma chave
            que não existe.
"""

# dic = {}
# print(dic['geek'])
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 130, in <module>
#     print(dic['geek'])
# KeyError: 'geek'

"""
AttributeError --> ocorre quando uma variável não tem um atributo/função

"""

tupla = (11, 2, 31, 4)
# print(tupla.sort()) # sort só funciona com lista
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 142, in <module>
#     print(tupla.sort())
# AttributeError: 'tuple' object has no attribute 'sort'

"""
IndentationError --> em Java e C a indentação não é obrigatória. Em Python.
                    este erro ocorre quando não respeitamos a indentação (4 espaços)
                    ou colocamos um print, por exemplo, dentro ou fora do loop.
                    
"""

# def nova():
# print('Geek')
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 156
#     print('Geek')
#     ^
# IndentationError: expected an indented block

# for i in range(10):
# i + 1
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\erros_mais_comuns_em_python.py", line 163
#     i + 1
#     ^
# IndentationError: expected an indented block

"""
Exceptions e Erros são sinônimos na programação.
"""