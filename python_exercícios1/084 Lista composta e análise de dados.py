pessoas = list()
dados = list()
pesados_nomes = list()
leves_nomes = list()

# Armazenado todos os dados na lisra de pessoas
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        print('Opção inválida!')
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break

# verificando os mais pesados e os mais leves
mais_leve = mais_pesado = float()
for indice,pessoa in enumerate(pessoas):
    # na primeira iteração
    if indice == 0:
        mais_leve = mais_pesado = pessoa[1]
        leves_nomes.append(pessoa[0])
        pesados_nomes.append(pessoa[0])

    elif pessoa[1] >= mais_pesado:
        if pessoa[1] > mais_pesado:
            pesados_nomes.clear()
            mais_pesado = pessoa[1]
        pesados_nomes.append(pessoa[0])

    elif pessoa[1] <= mais_leve:
        if pessoa[1] < mais_leve:
            leves_nomes.clear()
            mais_leve = pessoa[1]
        leves_nomes.append(pessoa[0])

# exibindo as estatísticas
print('✽' * 40)
print(f'➤Foram cadastradas {len(pessoas)} pessoas')
print(f'➤Maior peso de {mais_pesado}Kg: {pesados_nomes}')
print(f'➤Menór peso de  {mais_leve}Kg: {leves_nomes}')
