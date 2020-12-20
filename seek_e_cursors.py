"""
SEEK E CURSORS

seek() --> é utilizada para movimentar o cursor pelo arquivo
"""

arquivo = open('texto.txt')

print(arquivo.read(50))  # limita a leitura aos primeiros 50 caracteres

#print(arquivo.read())


# Movimentando o cursor pelo arquivo com a função seek()

"""
A função seek() é utilizada para movimentação do cursor pelo
arquivo. Ela recebe um parâmetro que indica onde queremos
colocar o cursor.
"""

#arquivo.seek(22)  # começa a ler do caractere 22

#print(arquivo.read())

# Leitura linha a linha: readline()

# print(arquivo.readline())  # imprime primeira linha
# print(arquivo.readline())  # imprime segunda linha
# print(arquivo.readline())  # imprime terceira linha
                           # ... e assim por diante

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))  # separa cada palavra por um espaço

# readlines() --> lê várias linhas
# cria uma lista onde cada linha é uma string
linhas = arquivo.readlines()
print(len(linhas))  # quantas linhas com conteúdo há no arquivo

"""
Quando abrimos um arquivo com a função open(), é criada uma conexão
entre o arquivo no disco C: e o nosso programa. Essa conexão é
chamada de streaming. Ao finalizar os trabalhos com o arquivo,
devemos fechar essa conexão. Para isso, utilizamos a função
close()

Passos para se trabalhar com um arquivo:
1 -- abrir o arquivo
2 -- trabalhar o arquivo
3 -- fechar o arquivo
"""

print(arquivo.closed)  # verifica se o arquivo está aberto (False) ou fechado (True)
arquivo.close()
print(arquivo.closed)
"""
Se não for fechado, o arquivo não poderá ser aberto por outro programa
porque está aberto no nosso programa (cria um lock).
"""

"""
Se tentarmos trabalhar no aarquivo depois que ele foi fechado,
teremos um ValueError
"""

