nome = str(input('Escreva um nome: ')).strip().title()
nome2 = nome.split()
palavras = len(nome2)
print('Primeiro nome: {}'.format(nome2[0]))
print('último nome: {}'.format(nome2[palavras - 1]))
