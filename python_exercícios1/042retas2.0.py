r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas digitadas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('As retas digitadas não podem formar um triângulo!')
