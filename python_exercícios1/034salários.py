salario = float(input('Salário actual: '))
if salario > 1250.00:
    print('Antigo salário: R${:.2f} \nAumento: 10%. \nNovo salário: R${:.2f}'.format(salario, (salario * 110) / 100))
elif salario <= 1250.00:
    print('Salário antigo: R${:.2f} \nAumento: 15%. \nNovo salário: R${:.2f}'.format(salario, (salario * 115) / 100))
