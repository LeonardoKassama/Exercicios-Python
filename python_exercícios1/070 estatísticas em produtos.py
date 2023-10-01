total = mais_de_mil = smaller_price = 0
smaller_p_name = str(' ')
while True:
    name = str(input('Nome do produto: '))
    price = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    # descobrindo o produto mais barato:
    if total == 0 or price < smaller_price:
        smaller_price = price
        smaller_p_name = name
    # total gasto na compra:
    total += price
    # produtos com mais de R$1000:
    if price > 1000:
        mais_de_mil += 1
    # interrompendo o loop:
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${total:.2f}')
print(f'Produtos custando mais de R$1000: {mais_de_mil}')
print(f'O produto mais barato é {smaller_p_name}, e custa R${smaller_price:.2f}')
