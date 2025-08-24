from math import *
import os
import app

def exibir(texto):
    """Essa função é para exibir"""
    os.system('cls')
    print(''.ljust(25) + (len(texto) + 1) * '-')
    print(''.ljust(25) + texto)
    print(''.ljust(25) + (len(texto) + 1) * '-')

def escolha_volume():
    """essa função é responsavel pela escolha do usuario"""
    try:
        print('------')
        print('Opção')
        print('-----')
        escolha_tipo = int(input('escolha 1 para calcular a volume do cubo \n e 2 para calcular o volume do paralelepipedo \n e 3 para calcular o volume do cilindro \n e 4 para calcular o volume do cone \n e 5 para calcular o volume da esfera \n 6 para sair:  '))

        if escolha_tipo == 1:
            cubo()
        elif escolha_tipo == 2:
            paralelepipedo()
        elif escolha_tipo == 3:
          cilindro()
        elif escolha_tipo == 4:
            cone()
        elif escolha_tipo == 5:
            esfera()
        elif escolha_tipo == 6:
            voltar()

        else:
         escolha_volume()
    except:
        escolha_volume()

"""As função abaixo são responaveis por calcular a área das seguinte formas geometricas abaixo"""

def cubo():
   exibir(texto='Calcular o volume do Cubo')
   lado = float(input('Qual a medida do lado do cubo: '))
   volume = pow(lado,3)
   print(f'O volume do cubo é {volume:.2f}³')
   sair()

def paralelepipedo():
    exibir(texto='Calcular o volume do Parelelepipedo')
    comprimeto = float(input('Qual é o comprimento do paralelepipedo: '))
    altura = float(input('Qual a altura do paralelepipedo: '))
    largura = float(input('Qual a largura do paralelepipedo'))
    volume = comprimeto * largura * altura
    print(f'O volume do paralelepipedo é {volume:.2f}³')
    sair()

def cilindro():
   exibir(texto='Calcular o volume do Cilindro')
   raio = float(input('Qual o raio do cilindro: '))
   altura = float(input('Qual a altura do cilindro: '))
   volume = pi * pow(raio, 2) * altura
   print(f'O volume do cilindro é {volume:.2f}³')
   sair()

def cone():
    exibir('Calcular volume do Cone')
    raio = float(input('Qual o raio do cone: '))
    altura = float(input('Qual a altura do cone: '))
    volume = (((pow(raio,2)) * altura) * pi / 3)
    print(f'O volume do cone é {volume:.2f}³')
    sair()

def esfera():
   exibir(texto='Calcular volume da Esfera')
   raio = float(input('Qual o raio da esfera: '))
   volume = (4/3) * pi * pow(raio,3)
   print(f'O volume da esfera é {volume:.2f}³')
   sair()

def sair():
    """Essa Função é para sair do da função"""
    input('digite algo para sair: ')
    os.system('cls')
    escolha_volume()
    
def fechar():
    """Essa função é para fechar o programa"""
    exibir(texto='Fechar programa')
    input('Digite algo para fechar o programa: ')

def voltar():
    input('Digite algo para voltar: ')
    os.system('cls')
    app.escolha()