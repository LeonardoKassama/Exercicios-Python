numero = int(input('Digite um número qualquer: '))
contador = numero - 1

print('{}!= {}'.format(numero, numero), end=' ')
while contador != 0:
    print('x {}'.format(contador), end=' ')
    if contador == numero - 1:
        produto = (contador + 1) * contador
    else:
        produto *= contador
    contador -= 1
print('=', produto)
