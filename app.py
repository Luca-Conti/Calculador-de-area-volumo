from Área_e_Volume.area import *
from Área_e_Volume.volume import *

def escolha():
    """essa função é responsavel pela escolha do usuario"""
    try:
        print('------')
        print('Opição')
        print('------')
        escolha_do_usuario = int(input('Escolha 1 para calcular a área e 2 para calcular o volume: '))
        if escolha_do_usuario == 1:
            escolha_area()
        elif escolha_do_usuario== 2:
            escolha_volume()
        else:
            escolha()
    except:
        escolha()

if __name__ == "__main__":
    exibir(texto='Calculadora de Área e Volume')
    escolha()