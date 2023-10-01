numero = int(input('Digite um número: '))
print('O dobro de {} é \033[1;34m{}\033[m'.format(numero, (numero*2)))
print('O triplo de {} é \033[1;35m{}\033[m'.format(numero, (numero*3)))
print('A raiz quadrada de {} é \033[1;31m{}\033[m'.format(numero, (numero**(1/2))))
