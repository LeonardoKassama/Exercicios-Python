matriz = [[],[],[]]

# colocando os valóres dentro da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valór para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
print(f'=-'*20)

# exibindo os resulatados em linhas e colunas
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^10}]', end=' ')
    # quebrando a continuidade da linha depois de uma linha
    print()
