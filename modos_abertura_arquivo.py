#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
"""
Modos de abertura de arquivo

r --> abre para leitura (padrão)
w --> abre para escrita (sobrescreve caso o arquivo já exista)

http://docs.python.org/3/library/functions.html#open

x --> abre para cescrita somente se o arquivo não existir. 
      Se o arquivo existir, gera FileExistsError
"""

"""
with open('university.txt', 'r') as arquivo:
    arquivo.write('Teste de conteúdo. \n')
except FileExistsError:
    print('Arquivo já existe')
"""

"""
a (append) --> abre para escrita adicionando o conteúdo ao final do 
               arquivo. Abrindo no modo a, se o arquivo não existir
               será criado. Caso exista, o novo conteúdo será 
               adicionado ao final.

"""
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

"""
O conteúdo SEMPRE é adicionado ao final do arquivo.
Não é possível controlar o cursor com o modo 'a'
"""

with open('outro.txt', 'a+') as arquivo:
    # arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Outra linha')

# + abre para o modo de atualização e deve ser acompanhado de
# outro comando.
# r+ substitui o conteúdo
# a+ adiciona o conteúdo no final
# w+ substitui o conteúdo

