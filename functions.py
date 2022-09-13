from random import *
from time import sleep

def inicio():
    saldo = uniform(200,10000)
    print('====' * 7)
    print('CAIXA ELETRONICO')
    print('SALDO NO CAIXA: R${:.2f}'.format(saldo))
    print('====' * 7)
    print(' ')
    
def converter(valor):
    if ',' in valor:
        valor = valor.replace(',','.')
        valor = float(valor)
        return valor
    elif '.' in valor:
        valor = float(valor)
        return valor