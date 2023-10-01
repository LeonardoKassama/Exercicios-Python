from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
data = date.today().year
idade = data - nascimento
if idade <= 9:
    print('Classificação: MIRIM')
elif 10 <= idade <= 14:
    print('Classificação: INFANTIL')
elif 15 <= idade <= 19:
    print('Classificação: JÚNIOR')
elif 20 <= idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
