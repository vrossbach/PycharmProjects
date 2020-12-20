#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
POO - PROPRIEDADES (PROPERTIES)

--> Em linguagens de programação como o Java, ao declarar
    atributos privados nas classes costumamos criar métodos
    públicos para a manipulação deste atributos.
    
    Estes métodos são conhecidos como getters e setters.
    
    Os getters retornam o valor do atributo e os setters
    alteram o valor do mesmo.
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

# Métodos públicos para ter acesso:
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Nunca faça:
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma dos saldos é {soma}')

# Forma correta:
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos é {soma}')

print(conta1.__dict__)
# {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 5000}
conta1.set_limite(99999)
print(conta1.__dict__)
# {'_Conta__numero': 1, '_Conta__titular': 'Felicity', '_Conta__saldo': 3000, '_Conta__limite': 99999}


"""
# REFATORANDO:

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

# DEFININDO UM MÉTODO COMO PROPRIEDADE:
    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.saldo)
print(conta2.saldo)
soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos é {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)  #76543

print(conta1.valor_total)
print(conta2.valor_total)