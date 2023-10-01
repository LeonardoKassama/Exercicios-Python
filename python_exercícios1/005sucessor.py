numero = int(input('Digite um número: '))
cores = {'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'limpo': '\033[m'}
print('O antecessor do numero digitado é: {}{}{}'.format(cores['azul'], numero-1, cores['limpo']))
print('O sucessor do número digitado é: {}{}{}'.format(cores['amarelo'], numero+1, cores['limpo']))
