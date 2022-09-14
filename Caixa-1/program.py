print("Caixa eletrônico")
print("Exemplo de valor: 175,45")
print(" ")

x = input("Qual valor deseja sacar? R$ " )
y = x.replace(",",".")
w = float(y) 
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
resultado = str(total)
total = resultado.replace(".", ",")
saldo = round(w, 2)

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
print("Totalizando: R$",total, "reais.")
print("Saldo restante: R$",saldo)
