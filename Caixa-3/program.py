x = float(input("Valor que deseja sacar: "))
z = x; y = [100, 50, 20, 10, 5, 2, 1]
for i in y:
    x = z // i; r = z % i; z = r
    print(x, 'Notas de:', i)
