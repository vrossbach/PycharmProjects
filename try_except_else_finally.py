"""
TRY, EXCEPT, ELSE, FINALLY

Dica de quando e onde tratar código:

Toda entrada do usuário deve ser tratada!
A função do usuário é destruir o seu sistema.
"""

num = None

try:
    num = int(input('informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}')

"""
A utilização de else e finally não é muito comum. 
"""

try:
    num = int(input('informe um número: '))
except ValueError:
    print('Valor incorreto')
else:  # é executado somente se não ocorrer o erro.
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

"""
--> O bloco finally é sempre executado, independente se houve
exceção ou não.
--> O finally geralmente é utilizado para fechar ou desalocar recursos.
"""

""" Forma bagunçada de tratar erros: """
def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

""" Os erros devem ser tratados dentro da definição da função: """

def multiplica(a, b):
    try:
        return a * b
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(multiplica(num1, num2))

""" 
Tratamento semi-genérico:
"""

def multiplica(a, b):
    try:
        return a * b
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    except NameError:
        return 'Valor incorreto'
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(multiplica(num1, num2))
