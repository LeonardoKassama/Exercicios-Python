numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        print('Opção inválida!\nTente novamente.')
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números.\nEsses números ordenados de forma decrescente ficam: {numeros}')
print('O número 5 está na lista? ',end='')
if 5 in numeros: print(f'Sim;\nE o número 5 foi digitado {numeros.count(5)} vezes')
else: print('Não.')
