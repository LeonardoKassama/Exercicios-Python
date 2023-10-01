cidade = str(input('Escreva o nome de uma cidade: '))
cidade1 = cidade.split()
print('Essa cidade começa com a palavra "Santo"? ')
print('SANTO' in cidade1[0].upper())
