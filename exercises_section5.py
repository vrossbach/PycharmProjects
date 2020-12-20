"""
1 - Recebe 2 números e mostrar o maior

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 < num2:
    print(f'{num2} é maior que {num1}.')
elif num1 == num2:
    print(f'Os dois números são iguais.')
else:
    print(f'{num1} é maior que {num2}')

2 - Raiz quadrada

num = float(input('Digite um número:'))
if num >=0:
    print(f'A raiz quadrada de {num} é {(num)**(1/2)}')
else:
    print(f'Não foi possível calcular a raiz quadrada de {num}.')


8 -

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if nota1 >= 0 and nota2 >= 0:
    print(f'A média das notas é {(nota1 + nota2)/2}')
else:
    print(f'Notas inválidas. Digite valores positivos.')

9 -

sexo = input('Sexo feminino: digite F; Sexo masculino: digite M.')
h = float(input('Qual a sua altura (em m)?'))
M = True
F = False
if sexo is True:
    print(f'O seu peso ideal é de {72.7*h - 58} kg.')
else:
    print(f'O seu peso ideal é de {62.1*h - 44.7} kg.')

11 -

num = input('Digite um número inteiro.')
if int(num) < 0:
    print('Número inválido.')
else:
    soma == {int(num[0]) + int(num[1]) + int(num[2])}
    print(soma)

Forma generalizada:
n = input('Digite um número inteiro: ')
print(sum(int(i) for i in n))

Outra forma:
numero = int(input('numero: '))
if numero > 0:
    soma = 0
    while numero != 0:
        resto = numero % 10
        numero = (numero - resto) // 10
        soma = soma + resto
    print(f'soma: {soma}')
else:
        print('numero invalido...')

13 -

nota1 = float(input('Digite a nota da P1: '))
nota2 = float(input('Digite a nota da P2: '))
nota3 = float(input('Digite a nota da P3: '))
media = (nota1 + nota2 + 2*nota3)/4
if media > 6.0:
    print(f'Sua média é {media}. Você foi APROVADO.')
else:
    print(f'Sua média é {media}. Você foi REPROVADO.')

15 -


dia = int(input('Digite o número correspondente ao dia da semana: '))
if dia == 1:
    print('Domingo')
elif dia==2:
    print('Segunda')
elif dia==3:
    print('Terça')
elif dia==4:
    print('Quarta')
elif dia==5:
    print('Quinta')
elif dia==6:
    print('Sexta')
elif dia==7:
    print('Sábado')
else:
    print('Fim do mundo')
"""

oper = int(input('Que operação você quer realizar? '
                 '1 - Adição '
                 '2 - Subtração '
                 '3 - Multiplicação '
                 '4 - Divisão '))
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
if oper == 1:
    print(f'{num1} + {num2} = {num1 + num2}')
elif oper == 2:
    print(f'{num1} - {num2} = {num1 - num2}')
elif oper == 3:
    print(f'{num1} * {num2} = {num1 * num2}')
elif oper == 4:
    print(f'{num1}/{num2} = {num1 / num2}')
