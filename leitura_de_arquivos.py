"""
LEITURA DE ARQUIVOS

--> Para ler o conteúdo de um arquivo em Python, usamos a função
integrada open(), que literalmente significa 'abrir'.:key

open() --> Na forma mais simples de utilização, nós passamos
           apenas um parâmetro de entrada, que neste caso é o
           caminho para o arquivo a ser lido. Essa função retorna um
           _io.TextIOWrapper e é com ele que trabalhamos então.

http://docs.python.org/3/library/functions.html#open

--> Por padrão, a função open() abre o arquivo para leitura. Este arquivo
    deve existir, ou então teremos o erro FileNotFoundError
"""

arquivo = open('texto.txt')

print(arquivo)
# <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# mode r --> modo leitura (read)
# encoding --> codificação em que o conteúdo do arquivo foi escrito
                # e deve ser lido. Com UTF-8, todos os caracteres
                # especiais são reconhecidos

print(type(arquivo))
# <class '_io.TextIOWrapper'>

""" Para ler o conteúdo de um arquivo, após sua abertura devemos
utilizar a função read().
"""

print(arquivo.read())

""" 
O Python utiliza um recurso para trabalhar com arquivos chamado
CURSOR, que funciona como o cursor quando estamos escrevendo.
Por isso o que já foi lido ficou para trás do cursor. Se a função
read() for repetida, não vai acontecer nada porque não existe nada para
ser lido após o cursor.
"""

"""
A função read() lê todo o conteúdo do arquivo.
"""

ret = arquivo.read()
print(type(ret))  # <class 'str'>
print(ret)  # Não acontece nada porque o conteúdo já foi lido.

arquivo.close()