class CisneNegro:

    def __len__(self):
        return 42

livro = CisneNegro()

print(len(livro))  # 42

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicionario = {"carlos": 12, "vanessa": 34, "joana": 49}

print(len(nome)) #15
print(len(lista)) # 4
print(len(dicionario)) # 3

# O tipo ou classe de objeto é menos importante que os métodos que o definem
# Ao invés de checar a classe ou tipo de dado, é checada a presença de métodos ou atributos específicos

# Os tipos acima são containers e têm o método len
# Objetos similares devem ter métodos ou atributos similares
