#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

"""
DECORADORES (Decorators)

--> Decorators são funções 
--> Envolvem outras funções e aprimoram seus comportamentos
--> Decorator remete a decoração
--> Decorators também são exemplos de HOF
--> Têm uma sintaxe própria usando @ (syntax sugar ou açúcar sintático)

---------------------------
    Function Decorator
---------------------------

---------------------------
  -----------------------
    Função decorada
  -----------------------
---------------------------

"""

# DECORATORS COMO FUNÇÕES (sintaxe não recomendada, sem sugar)

def seja_educado(funcao):
    def sendo():
       print('Foi um prazer conhecer você!')
       funcao()
       print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Teste

teste = seja_educado(saudacao)
teste()

# Foi um prazer conhecer você!
# Seja bem-vindo(a) à Geek University
# Tenha um ótimo dia!

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)
raiva_educada()

# ----------------------------------------------------

# DECORATORS COM SYNTAX SUGAR

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir')

dormir()

"""
|-----------------------------------------------------
|  Home  |  Serviços  |  Produtos  |  Administrativo  |

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

Obs.: não é código funcional

def checa_login():
    if not request.usuario:
        redirect('http://suaempresa.com.br')

def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login    
def admin (request):
    return 'Pode acessar admin'
"""

# OBS.: não confundir com Decoration Function (é a função decoradora)
# o decorator é a função que recebe o @ e é decorada