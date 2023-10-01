from datetime import date
ano = int(input('Digite um ano qualquer: \nColoque 0 para analizar o ano actual! '))
if ano == 0:
    ano = date.today().year  # isso nos permite acessar o ano actual do computador.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} ñ é bissexto.'.format(ano))
