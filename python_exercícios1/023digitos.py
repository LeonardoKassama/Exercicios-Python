valor = int(input('Digite um número de 0 a 9999: '))
# Aquí nós usamos uma fórmula matemática.
print('Unidade: {}'.format(valor // 1 % 10))
print('Desena: {}'.format(valor // 10 % 10))
print('Centena: {}'.format(valor // 100 % 10))
print('Milhar: {}'.format(valor // 1000 % 10))
