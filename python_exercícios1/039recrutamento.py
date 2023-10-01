#Sugestão:
# -destinguir se é homem ou mulher;
# -saber em que ano foi o alistamento.
from datetime import date
data = int(input('Escreva o seu ano de nascimento: '))
atual = date.today().year

# A idade é adquerida com a formula "(atual - data)".
if (atual - data) < 18:
    print('Você ainda vai ter que se alistar ao serviço militar')
    print('Faltam {} anos'.format(18 - (atual - data)))
elif (atual - data) > 18:
    print('Você já passou do tempo de se alistar')
    print('Já se passaram {} anos'.format((atual - data) - 18))
elif (atual - data) == 18:
    print('Já é hora de se alistar!')
