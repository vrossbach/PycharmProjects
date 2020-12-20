"""
WALRUS --> atribuição e retorno de valor em uma mesma expressão

variavel := expressão

Parece com o MathCad

print(nome := 'Geek University')

base = 5
altura = 10

print(area := base * altura)

# Python 3.7
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')
"""

# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ') != 'jaca'):
    cesta.append(fruta)
