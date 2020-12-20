"""
SET COMPREHENSION
Lista = [1,2,3,4]
Set = {1,2,3,4}
--> Set não aceita valores repetidos e não guarda a ordenação dos valores.

"""

numeros = {num for num in range(1, 7)}
print(numeros)
# {1, 2, 3, 4, 5, 6}

numeros2 = {x ** 2 for x in range(10)}
print(numeros2)
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set.

numeros3 = {x: x ** 2 for x in range(10)}
print(numeros3)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

letras = {letra for letra in 'Geek University'}
print(letras)
# {'v', ' ', 't', 'G', 'U', 'e', 's', 'y', 'r', 'n', 'i', 'k'}
