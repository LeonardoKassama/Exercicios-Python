from datetime import date
agora = date.today().year
contador1 = 0
contador2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}ª pessoa? '.format(c)))
    if agora - ano >= 21:
        contador1 += 1
    else:
        contador2 += 1
print('Maiores de idade: {}\nMenóres de idade: {}'.format(contador1, contador2))
