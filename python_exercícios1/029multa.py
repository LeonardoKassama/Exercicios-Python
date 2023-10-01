velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Ultrapassaste a velocidade recomendada! \nTens uma multa de R${:.2f}'.format(multa))
else:
    print('Vc respeitou os limites de velocidade. \nFoste um bom cidadão !')
