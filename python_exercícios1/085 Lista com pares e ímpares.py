valores = [[],[]]
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valór: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Valores pares digitados: {valores[0]} \nValores ímpares digitados: {valores[1]}')
