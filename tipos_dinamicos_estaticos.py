# Tipagem de dado implícita ou dinâmica:

# idade = 42
# print(type(idade))
# <class 'int'>

# idade = 'quarenta e dois'
# print(type(idade))
# <class 'str'>

# Mas se converter int em string vai resultar em '42'

# Problema da tipagem dinâmica:
# if True:
#    resultado = 1 + 'Geek'
# else:
#    resultado = 1 + 41
# print(resultado)

# Na tipagem estática, uma variável não pode ter seu tipo
# alterado durante o programa