"""
Introdução ao módulo Unittest

--> Teste unitários: usados para testar unidades individuais
    de código-fonte.

--> Unidades individuais podem ser:
    funções;
    métodos;
    classe;
    módulos, etc.

--> Teste unitário não é específico da linguagem Python.

--> Para criar nossos testes, criamos classes que herdam de
    unittest.TestCase e, a partir de então, ganhamos todos
    os assertions presentes no módulo.

--> Para rodar os testes, utilizamoms uittest.main()

--> TestCase: casos de teste para a sua unidade

Conhecendo as assertions:

assertionEqual(a, b)     checa se a == b
asserNotEqual(a, b)         a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIsNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIn(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsInstance(a, b)      a é instância de b
assertNotIsInstance(a, b)   a não é instância de b

Por convenção, todos os testes em um TestCase devem ter seu nome iniciado com
test_

Para executar os testes com unittest:

python nome_do_modulo.py

Para executar os testes no modo verbose:

python nome_do_modulo -v

--> Podemos acrescentar (e é recomendado) docstrings nos nossos testes.

"""


# Usando TDD

# atividades.py e testes.py

