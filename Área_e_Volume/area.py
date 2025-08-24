"""Esse arquivo é para calcular a área"""
from math import *
import os
import app

def exibir(texto):
    """Essa função é para exibir"""
    os.system('cls')
    print(''.ljust(25) + (len(texto) + 1) * '-')
    print(''.ljust(25) + texto)
    print(''.ljust(25) + (len(texto) + 1) * '-')

def escolha_area():
    """essa função é responsavel pela escolha do usuario"""
    try:
        print('-----')
        print('Opção')
        print('-----')
        escolha_tipo = int(input('escolha 1 para calcular a área do circulo \n e 2 para calcular a área do trapezio \n e 3 para calcular a área do quadrado \n e 4 para calcular a área do retangulo\n e 5 para calcular a área do triângulo\n e 6 para calcular a área do losangulo \n e 7 para voltar:  '))

        if escolha_tipo == 1:
            circulo()
        elif escolha_tipo == 2:
            trapezio()

        elif escolha_tipo == 3:
          quadrado()

        elif escolha_tipo == 4:
            retangulo()
        elif escolha_tipo == 5:

            triagulo()

        elif escolha_tipo == 6:
            losangulo()
        elif escolha_tipo == 7:
         voltar()

        else:
         escolha_area()
    except:
        escolha_area()
"""As função abaixo são responaveis por calcular a área das seguinte formas geometricas abaixo"""
def circulo():
    exibir(texto='Calcular á Área do circulo')
    diametro = float(input('Qual o diametro do circulo: '))
    area = pi * pow(diametro,2)
    print(f'A área do circulo é {area:.2f}²')
    sair()

def trapezio():
    exibir(texto='Calcular a Área do trapezio')
    Base = float(input('Digte a base do trapezio: '))
    base = float(input('Digte a base do trapezio: '))
    altura = float(input('Digite a altura do trapezio: '))
    area = (base + Base) * altura /2
    print(f'A área do trapezio é {area:.2f}²')
    sair()

def quadrado():
    exibir(texto='Calcular a Área do quadrado')
    lado = float(input('Qual a medida do lado do quadrado: '))
    area = pow(lado,2)
    print(f'A área do quadrado é {area:.2f}²')
    sair()

def retangulo():
    exibir(texto='Calcular a Área do retangulo')
    base = float(input('Digte a base do retangulo: '))
    altura = float(input('Digite a altura do retungulo: '))
    area = base * altura
    print(f'A área do retangulo é {area:.2f}²')
    sair()

def triagulo():
    exibir(texto='Calcular a Área do triângulo')
    base = float(input('Digte a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))
    area = (base * altura) /2
    print(f'A área do triângulo é {area:.2f}²')
    sair()

def losangulo(): 
    exibir(texto='Calcaulador de Área do losangulo')
    Diagonal = float(input('Qual a diagonal maior do losangulo: '))
    diagonal = float(input('Qual a diagonall menor do losangulo'))
    area = (diagonal * Diagonal) /2
    print(f'A área do losangulo é {area:.2f}²')
    sair()

def sair():
    """Essa Função é para sair do da função"""
    input('digite algo para sair: ')
    os.system('cls')
    escolha_area()
    
def fechar():
    """Essa função é para fechar o programa"""
    exibir(texto='Fechar programa')
    input('Digite algo para fechar o programa: ')

def voltar():
    input('Digite algo para voltar: ')
    os.system('cls')
    app.escolha()