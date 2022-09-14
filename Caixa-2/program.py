from random import *
from time import sleep

saldo = uniform(200,10000)

print ('===' * 7)
print('Caixa eletrônico')
print('Saldo: R${:.2f}'.format(saldo))
print ('===' * 7)
print(' ')

menu = True
while(menu):
    valor = input('Valor que deseja sacar: R$')
    if '.' in valor:
        valorConvertido = float(valor)
        menu = False
    elif ',' in valor:
        b = valor.replace(',', '.')
        valorConvertido = float(b)
        menu = False
    else:
        print('invalido')
        
        continuar = input('Deseja continuar? S/N ')
        
        if continuar == 'S' or 's':
            menu = True
        elif continuar == 'N' or 'n':
            menu = False
            quit()
        else:
            print('Invalido')
            print('Encerrando...')
            quit()
            
# ------------------------------ 
quantCem = valorConvertido // 100
resto = valorConvertido % 100

quantCinquenta = resto // 50
resto = resto % 50

quantVinte = resto // 20
resto = resto % 20

quantDez = resto // 10
resto = resto % 10

quantCinco = resto // 5
resto = resto % 5

quantDois = resto // 2
resto = resto % 2

sobra = saldo - valorConvertido

# ------------------------------
print ('===' * 7)
print('CONTANDO CÉDULAS...')

sleep(2)

if quantCem > 0:
    print('Quantidade de notas de R$100,00:', quantCem)
    sleep(1)
if quantCinquenta > 0:
    print('Quantidade de notas de R$50,00:', quantCinquenta)
    sleep(1)
if quantVinte > 0:
    print('Quantidade de notas de R$20,00:', quantVinte)
    sleep(1)
if quantDez > 0:
    print('Quantidade de notas de R$10,00:', quantDez)
    sleep(1)
if quantCinco > 0:
    print('Quantidade de notas de R$5,00:', quantCinco)
    sleep(1)
if quantDois > 0:
    print('Quantidade de notas de R$2,00:', quantDois)
if resto < 2:
    resto = round(resto,2)
    print('Restante: R${:.2f}'.format(resto))
if sobra > 0:
    print('Valor disponível no caixa: R${:.2f}'.format(sobra))
    print ('===' * 7)
else:
    print('Sem saldo no caixa.')
    print ('===' * 7)

	
