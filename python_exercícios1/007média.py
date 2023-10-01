nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua primeira nota é {} \nA sua segunda nota é {}'.format(nota1, nota2,))
cores = {'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'limpo': '\033[m'}
if media >= 12:
    print('A tua média é de {}{}'.format(cores['verde'], media))
else:
    print('A tua média é de {}{}'.format(cores['vermelho'], media))
