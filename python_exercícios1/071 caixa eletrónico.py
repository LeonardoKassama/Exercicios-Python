cedulas_de50 = cedulas_de20 = cedulas_de10 = cedulas_de1 = 0

print('{:^40}'.format('＄ TRIBAL BANK ＄'))
while True:
    if cedulas_de50 == 0:
        valor_do_saque = int(input('Introduza o valór que deseja sacar: R$'))
        diferenca_de_saque = valor_do_saque

# verificando quantas cedulas de R$50:
    if diferenca_de_saque >= 50:
        cedulas_de50 += 1
        diferenca_de_saque -= 50

# verificando quantas cedulas de R$20:
    if 49 >= diferenca_de_saque >= 20:
        cedulas_de20 += 1
        diferenca_de_saque -= 20

# verificando quantas cedulas de R$10:
    if 19 >= diferenca_de_saque >= 10:
        cedulas_de10 += 1
        diferenca_de_saque -= 10

# verificando quantas cedulas de R$1:
    if 9 >= diferenca_de_saque >= 1:
        cedulas_de1 += 1
        diferenca_de_saque -= 1
# interrompendo o loop:
    if diferenca_de_saque == 0:
        break

if cedulas_de50 > 0:
    print(f'▻ Cedulas de R$50: {cedulas_de50}')
if cedulas_de20 > 0:
    print(f'▻ Cedulas de R$20: {cedulas_de20}')
if cedulas_de10 > 0:
    print(f'▻ Cedulas de R$10: {cedulas_de10}')
if cedulas_de1 > 0:
    print(f'Cedulas de R$1: {cedulas_de1}')
