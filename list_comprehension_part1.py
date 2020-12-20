"""
LIST COMPREHENSION

- Utilizando list comprehension, nós podemos gerar novas listas com dados processados
    a partir de outro iterável.

SINTAXE DA LIST COMPREHENSION

[dado for dado in iteravel]
"""

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
# [10, 20, 30, 40, 50]

"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em 2 partes:

1 - for numero in numeros
2 - numero * 10
"""

res2 = [numero / 2 for numero in numeros]

print(res2)


# [0.5, 1.0, 1.5, 2.0, 2.5]

def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]

print(res3)
# [1, 4, 9, 16, 25]

"""
LIST COMPREHENSION VERSUS LOOP
"""

# Loop:
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List comprehension:
print([numero*2 for numero in numeros])
# [2, 4, 6, 8, 10]

# Outros exemplos:

nome = 'Geek University'

print([letra.upper() for letra in nome])
# ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo[0:].upper() for amigo in amigos])
# ['MARIA', 'JULIA', 'PEDRO', 'GUILHERME', 'VANESSA']

print([amigo[0:].title() for amigo in amigos])
# ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(amigo) for amigo in amigos])
# ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

print([numero*3 for numero in range(1,10)])
# [3, 6, 9, 12, 15, 18, 21, 24, 27]

print([bool(valor) for valor in [0,[],'',True,1,3.14]])
# [False, False, False, True, True, True]

print([str(numero) for numero in numeros])
# ['1', '2', '3', '4', '5']