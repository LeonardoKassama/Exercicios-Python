km = float(input('Kilómetros percorridos: '))
dias = int(input('Número de dias: '))
# fórmula: (km * 0.15)+(dias * 60)
print('O valór a pagar pelo aluguel é de R${:.2f}'.format((km * 0.15)+(dias * 60)))
