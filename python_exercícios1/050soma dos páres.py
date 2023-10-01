soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}˚ valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
print('A soma de todos os números pares que estão presentes na lista acima é: {}'.format(soma))
