valores = list()
while True:
    valores.append(int(input('Digite um número qualquer: ')))
    resposta = str(input('Deseja digitar mais uma vez? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        print('Opção inválida!')
        resposta = str(input('Deseja digitar mais uma vez? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
pares = list()
impares = list()
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Números digitados: {valores}\nPares: {pares}\nÍmpares: {impares}')
