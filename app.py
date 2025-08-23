from math import *
import os
def exibir(texto):
    os.system('cls')
    print(''.ljust(25) + (len(texto) + 1) * '-')
    print(''.ljust(25) + texto)
    print(''.ljust(25) + (len(texto) + 1) * '-')

    

def escolha():
    """essa função é responsavel pela escolha do usuario"""
    try:
        print('-----')
        print('Opção')
        print('-----')
        escolha_tipo = int(input('escolha 1 para calcular a área do circulo \n e 2 para calcular a área do trapezio \n e 3 para calcular a área do quadrado \n e 4 para calcular a área do retangulo\n e 5 para calcular a área do triângulo\n 6 para sair:  '))

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
         fechar()

        else:
         escolha()
    except:
        escolha()

def circulo():
    exibir(texto='Calcular á Área do circulo')
    diametro = float(input('Qual o diametro do circulo: '))
    area = pi * pow(diametro,2)
    print(f'A área do circulo é {area}²')
    sair()

def trapezio():
    exibir(texto='Calcular a Área do trapezio')
    Base = float(input('Digte a base do trapezio: '))
    base = float(input('Digte a base do trapezio: '))
    altura = float(input('Digite a altura do trapezio: '))
    area = (base + Base) * altura
    print(f'A área do trapezio é {area}²')
    sair()

def quadrado():
    exibir(texto='Calcular a Área do quadrado')
    lado = float(input('Qual a medida do lado do quadrado: '))
    area = pow(lado,2)
    print(f'A área do quadrado é {area}²')
    sair()


def retangulo():
    exibir(texto='Calcular a Área do retangulo')
    base = float(input('Digte a base do retangulo: '))
    altura = float(input('Digite a altura do retungulo: '))
    area = base * altura
    print(f'A área do retangulo é {area}²')
    sair()

def triagulo():
    exibir(texto='Calcular a Área do triângulo')
    base = float(input('Digte a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))
    area = (base * altura) /2
    print(f'A área do triângulo é {area}²')
    sair

def sair():
    input('digite algo para sair: ')
    
def fechar():
    exibir(texto='Fechar programa')
    input('Digite algo para fechar o programa')

if __name__ == '__main__':
    exibir('Calcular Área')
    escolha()