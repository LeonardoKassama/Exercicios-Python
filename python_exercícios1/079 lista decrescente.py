numeros = list()
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Número adicionado com sucesso!')
    else:
        print('Valór duplicado! Não pode ser adicionado.')
    resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('OPÇÃO INVÁLIDA!')
        resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
numeros.sort()
print(f'Foram digitados os números: {numeros}')
