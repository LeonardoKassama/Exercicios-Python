from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
# Nesse caso usamos o método "shuffle". Que significa embaralhar.
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
