frase = str(input('Digite uma frase qualquer. ')).strip().upper().split()
fraseFinal = ''.join(frase)
inverso = ''  # criamos básicamente um contador mas só que de string.
for i in range(len(fraseFinal)-1, -1, -1):
    inverso += fraseFinal[i]
# também poderiamos ter usado um método de fatiamento ao invés do "for loop".
# da seguinte maneira:
# inverso = fraseFinal[::-1] → o que fizemos aquí foi fatiar do início ao fim, de trás pra frente.
print('O inverso de {} é {}'.format(fraseFinal, inverso))
if inverso == fraseFinal:
    print('A frase é um palindromo!')
else:
    print('A frase ñ é um palindromo!')
