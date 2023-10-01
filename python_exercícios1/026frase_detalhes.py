frase = str(input('Digite uma frase qualquer: ')).strip()
print('A letra "A" apareceu {} vezes na frase.'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.upper().find('A') + 1))
# Nesse caso usamos metodo "rfind" para procurar a partir da direita
print('Ela aparece pela última vez na posição {}.'.format(frase.upper().rfind('A') + 1))
