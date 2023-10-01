print('{:^30}'.format('TRIBAL STORE'))
price = int(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/ cheque.
[2] À vista no cartão.
[3] Em até 2X no cartão.
[4] 3X ou mais no cartão.''')
escolha = int(input('Escolha um método de pagamento: '))

# À vista dinheiro/ cheque.
if escolha == 1:
    ajuste = (price * 10) / 100
    print('Preço normal: {:.2f}\nDesconto: 10%\nPreço a pagar: {:.2f}'.format(price, price - ajuste))

# À vista no cartão.
elif escolha == 2:
    ajuste = (price * 5) / 100
    print('Preço normal: {:.2f}\nDesconto: 5%\nPreço a pagar: {:.2f}'.format(price, price - ajuste))

# 2x no cartão.
elif escolha == 3:
    print('Preço normal: {}\nJuros: 0%\nPreço a pagar(por parcela): {}'.format(price, price / 2))

# 3x ou mais no cartão.
elif escolha == 4:
    parcelas = int(input('Número de parcelas: '))
    if parcelas < 3:
        print('Escolha inválida!')
    elif parcelas >= 3:
        total = price + (price * 20 / 100)
        print('''Preço normal: {:.2f}\nJuros: 20%\nPreço total: {:.2f}\nPreço a pagar(por parcela): {:.2f}'''
              .format(price, total, total / parcelas))

# Escolha inválida.
else:
    print('Escolha inválida!!')
