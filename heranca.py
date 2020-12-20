#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO - HERANÇA (Inheritance)

--> Possibilidade de reaproveitar código e estender nossas classes.
--> Com a herança, a partir de uma classe existente nós
    estendemos outra classe que passa a herdar atributos
    e métodos da classe herdada.

2 entidades ou classes com seus atributos:
   
Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


Existe alguma entidade genérica o suficiente para encapsular os
atributos e métodos comuns a outras entidades?

--> Quando uma classe herda de outra classe, ela herda
    todos os atributos e métodos da classe herdada.
--> Quando uma classe herda de outra classe, a classe
    herdada é conhecida como superclasse, classe-mãe,
    classe-pai, classe base ou classe genérica.
--> Quando uma classe herda de outra classe, ela é chamada
    [Cliente, Funcionario]
    - Sub-classe
    - Classe filha
    - Classe específica

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """ Cliente herda de Pessoa """

    # Forma menor comum de acessar dados da super classe
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    """ Funcionário herda de Pessoa """

    # Forma comum de acessar dados da super classe
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

# OVERRIDING:
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} \nNome: {self._Pessoa__nome}'

"""
SOBRESCRITA DE MÉTODOS (OVERRIDING)
--> Ocorre quando reescrevemos um método presente na 
    superclasse em classes filhas.
"""

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
# {'_Pessoa__nome': 'Angelina', '_Pessoa__sobrenome': 'Jolie', '_Pessoa__cpf': '123.456.789-00', '_Cliente__renda': 5000}
# {'_Pessoa__nome': 'Felicity', '_Pessoa__sobrenome': 'Jones', '_Pessoa__cpf': '987.654.321-11', '_Funcionario__matricula': 1234}



