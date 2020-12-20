#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO - ABSTRAÇÃO E ENCAPSULAMENTO

--> O grande objetivo da POO é encapsular nosso código dentro
de um grupo lógico e hierárquico utilizando classes.


           CLASSE
---------------------------
|    ATRIBUTOS E MÉTODOS  |
---------------------------

--> Atributos/métodos privados em Python
    --> Imagine uma classe chamada Pessoa contendo um 
        atributo provado chamado __nome e um método
        privado chamado __falar. Estes métodos só 
        deveriam ser acessados dentro da classe, mas
        o Python não bloqueia este acesso (Name MangLing):
        
        _Classe__elemento
        instancia._Pessoa__nome
        instancia._Pessoa__falar()

--> ABSTRAÇÃO
    Ato de expor apenas dados relevantes de uma classe,
    escondendo atributos e métodos privados de usuário.
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}.')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
          if self.__saldo >= valor:
              self.__saldo -= valor
          else:
              print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo.')

    def transferir(self, valor, conta_destino):
        # 1 - remover valor da ocnta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferência paga por quem realizou a transferência
        # 2 - adicionar o valor à conta de destino
        conta_destino.__saldo += valor


conta1 = Conta('Angelina', 150, 3000)
conta2 = Conta('Felicity',300, 2000)

# CUIDADO: se deixarmos os atributos públicos, eles podem
# também ser modificados (mas com MangLing ainda é possível)

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()