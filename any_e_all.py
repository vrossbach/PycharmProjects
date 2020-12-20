"""
ANY e ALL

--> builtins

all() --> retorna True se todos os elementos do iterável forem verdadeiros
            ou se o iterável estiver vazio.
"""

print(all([0, 1, 2, 3, 4])) # Todos os valores são True? Não, o zero é False.
# False

print(all([1,2,3,4]))
# True

print(all([]))
# True

print(all((1,2,3,4)))
# True

print(all('Geek'))
# True

nomes = ['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all(nome[0] == 'C' for nome in nomes))  # É case sensitive

print(all([letra for letra in 'eio' if letra in 'aeiou']))
# True

print(all([letra for letra in 'TGCG' if letra in 'ATGCCGAAATTTGCG']))
# True

# Obs.: Um iterável vazio convertido em Boolean é False, mas o all() entende como True

print(all(numero for numero in [4, 2, 10, 6, 8] if numero %2 == 0))
# True

"""
any() retorna True se QUALQUER elemento deste for verdadeiro. 
Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False

print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([num for num in [4,2,10,6,8,9] if num % 2 == 0]))  # True
