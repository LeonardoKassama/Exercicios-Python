valores = list()
for i in range(0, 5):
    valor = int(input('Digite um valór: '))
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado no final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista.')
                break
            posicao += 1

print(f'Os valóres digitados em ordem foram: {valores}')