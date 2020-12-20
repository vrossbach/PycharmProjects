"""
LENDO ARQUIVOS CSV

CSV - Comma Separated Values (Valores Separados por Vírgula)

--> Podemos ter outros tipos de separadores além da vírgula:
    --> 1,2,3,4,5
    --> "geek", "university", "python", "ciência", "dados"
    --> 1;2;3;4;5
    --> 1 2 3 4 5

Podemos conseguir dados em:
    http://dados.gov.br/dataset
    
# LIMPEZA DE DADOS: modo mais trabalhoso
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

--> A linguagem Python possui duas formas diferentes para
    ler dados em arquivos csv:
    --> reader: permite iterar sobre as linhas do arquivo csv
        como listas
    --> DictReader: permite iterar sobre as linhas do arquivo
        csv como se fossem OrderedDicts
"""

# LIMPEZA DE DADOS: forma correta

# Reader:

from csv import reader
# OBS.: UTF-8 não está reconhecendo acentos do CSV
with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    print(type(leitor_csv))  # <class '_csv.reader'>
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cm.')

# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s){linha['Pais']} e mede {linha['Altura (em cm)']} cm.")

# Por padrão, estes dois métodos usam a vírgula como delimitador.
# Para usar outro separador, acrescentamos um parâmetro delimiter:

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s){linha['Pais']} e mede {linha['Altura (em cm)']} cm.")
