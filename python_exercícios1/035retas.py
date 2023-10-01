r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
# para ser capaz de formar um triângulo,
# cada uma das rectas deve ser menor que a soma do comprimenro dos outras duas.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    resposta = 'Podem formar um triângulo'
else:
    resposta = 'Não podem formar um triângulo'
print('As retas digitadas {}'.format(resposta))
