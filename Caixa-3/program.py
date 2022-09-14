import functions
functions.inicio()
valor = input("Valor que deseja sacar: ")
x = functions.converter(valor)
z = x; y = [100, 50, 20, 10, 5, 2]
for i in y:
    x = z // i; r = z % i; z = r
    print(x, 'Notas de:', i)
