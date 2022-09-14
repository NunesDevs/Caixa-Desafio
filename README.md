# Caixa-Desafio
## Propósito:
### Me desafiar simplificando meu código inicial. 
### Desafio de criar um sistema de caixa no qual os valores de saque são em notas de 100, 50, 20, 10, 5 e 2.


##### Primeira versão contem 66 linhas de código, design simples e funcionalidade simples.</p>
- [Script completo da primeira versão](https://github.com/NunesDevs/Caixa-Desafio/Caixa-1)
###### Lógica:
```bash
w = float(input("Qual valor deseja sacar? R$ " )) 
c = 0 
d = 0 
dd = 0
ddd = 0
u = 0 
uu = 0

if w >= 2.0:
    while(w >= 100.00):
        w = w - 100.00
        c = c + 1
    while(w >= 50.00):
        w = w - 50.00
        d = d + 1
    while(w >= 20.00):
         w = w - 20.00
         dd = dd + 1
    while (w >= 10.00):
        w = w - 10.00
        ddd = ddd + 1
    while(w >= 5.00):
        w = w - 5.00
        u = u + 1
    while(w >= 2.00):
        w = w - 2.00
        uu = uu + 1
elif w <= 1.99 and w > 0.0:
    print("Impossível sacar o valor. R$",w)
    quit()
else:
    print ("Valor inválido")
    quit()

total = c * 100.00 + d * 50.00 + dd * 20.00 + ddd * 10.00 + u * 5.00 + uu * 2.00
print("Você vai receber:")
if c > 0:
    print(c, "notas de R$ 100,00")
if d > 0:
    print(d, "notas de R$ 50,00")
if dd > 0:
    print (dd, "notas de R$ 20,00")
if ddd > 0:
    print(ddd, "notas de R$ 10,00")
if u > 0:
    print (u, "notas de R$ 5,00")
if uu > 0:
    print(uu, "notas de R$ 2,00")
```

##### Segunda versão contem 89 linhas de código, com melhor design e funcionalidade.
- [Script completo da segunda versão](https://github.com/NunesDevs/Caixa-Desafio/Caixa-2)
###### Lógica:
```bash
valor = float(input("Valor: "))
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
if quantCem > 0:
    print('Quantidade de notas de R$100,00:', quantCem)
if quantCinquenta > 0:
    print('Quantidade de notas de R$50,00:', quantCinquenta)
if quantVinte > 0:
    print('Quantidade de notas de R$20,00:', quantVinte)
if quantDez > 0:
    print('Quantidade de notas de R$10,00:', quantDez)
if quantCinco > 0:
    print('Quantidade de notas de R$5,00:', quantCinco)
if quantDois > 0:
    print('Quantidade de notas de R$2,00:', quantDois)
if resto < 2:
    resto = round(resto,2)
    print('Restante: R${:.2f}'.format(resto))
```

##### Terceira versão contem 5 linhas, focado no objetivo de dar a esperada saída, sem design e funcionalidades.
- [Script completo da terceira versão](https://github.com/NunesDevs/Caixa-Desafio/Caixa-3)
###### Lógica:
```bash 
valor = float(input("Valor que deseja sacar: "))`
x = valor
y = [100, 50, 20, 10, 5, 2]
for i in y:
    valor = x // i; r = x % i; x = r
    print(valor, 'Notas de:', i)
```
