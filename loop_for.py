"""
ESTRUTURAS DE REPETIÇÃO
1 - Loop for

Loop -> são estruturas de repetição
For -> uma destas estruturas de repetição

C ou Java:

for(int i = 0); i < limitador; i++){
    //execução do loop
}

Python:

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.
Exemplos de iteráveis:
- String: valor iterável entre seus caracteres -> [0], [1], ... ver exercício seção 5
- Lista: [0, 1, 2]
- Range: numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10) # temos que transformar em lista

# Exemplo de for 1: iterando sobre string
for letra in nome:
    print(letra) # imprime todas as letras do string separadas

# Exemplo de for 2: iterando em lista
for numero in lista:
    print(numero) # imprime todos os números da lista separados

# Exemplo de for 3: iterando sobre range
for numero in range(1, 10):
    print(numero) # imprme de 1 a 9


range(valor_inicial, valor_final)
Obs.: O valor final não é incluído

for i, v in enumerate(nome): # retorna um objeto do tipo enumerate
    print(nome[i])

Enumerate: atribui um índice para cada sequência do enumerável
((0, 'G'), (1, 'e') ...) -> gera uma tupla

# Outra forma:
for indice, letra in enumerate(nome):
    print(nome[indice])

# Outra forma:
for indice, letra in enumerate(nome):
    print(letra)

# Outra forma:
for _, letra in enumerate(nome): # _: descarta índice e imprime letra
    print(letra)

Obs.: quando não precisamos de um valor, podemos descartá-lo usando um _

----
for valor in enumerate(nome):
    print(valor)

(0, 'G')
(1, 'e')
(2, 'e')
(3, 'k')
(4, ' ')
(5, 'U')
(6, 'n')
(7, 'i')
(8, 'v')
(9, 'e')
(10, 'r')
(11, 's')
(12, 'i')
(13, 't')
(14, 'y')

for valor in enumerate(nome): # imprime somente os índices
    print(valor[0]) # [1] retorna somente letras
# Outros usos do for:

qtd = int(input('Quantas vezes este loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o valor {n} de {qtd}: '))
    soma = soma + num
print(f'A soma é {soma}.')
nome = 'Geek University'
for letra in nome:
    print(letra, end='')
nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de emojis unicode:
https://apps.timwhitlock.info/emoji/tables/unicode
Para imprimir emojis precisamos do seu caractere unicode
"""
# unicode original: U+1F638
# unicode modificado: U0001F638
emoji = 'U0001F646'
for _ in range(1):
    for num in range(1, 11):
        print('\U0001F648' * num)

