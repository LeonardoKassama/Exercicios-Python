valores = list()

for i in range(0, 5):
    valores.append(int(input('Digite um valór: ')))
# maior valór
print(f'Maior valór: {max(valores)}, na posição: ', end=' ')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(indice, end=', ')
# menór valór
print(f'\nMenór valór: {min(valores)}, na posição: ', end=' ')
for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(indice, end=', ')