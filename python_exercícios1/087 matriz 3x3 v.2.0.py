matriz = [[],[],[]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('=-'*20)
somatorio = somatorio_3c = maior_val_2l = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        # somatorio de todos os valores da matriz
        somatorio += matriz[linha][coluna]
        # somatorio dos valóres da 3ª colulna
        if coluna == 2:
            somatorio_3c += matriz[linha][coluna]
        # maior valore da 2ª linha
        if linha == 1:
            if coluna == 1:
                maior_val_2l = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maior_val_2l:
                    maior_val_2l = matriz[linha][coluna]
    print()
print('_' * 40)
print(f'''➤ Soma dos valores digitados: {somatorio}
➤ Soma dos valores da 3ª coluna: {somatorio_3c}
➤ Maior valor da 2ª linha: {maior_val_2l}''')
