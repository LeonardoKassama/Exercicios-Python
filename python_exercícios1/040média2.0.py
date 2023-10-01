nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO!!')
elif media >= 7.0:
    print('APROVADO!!')
# "5.0 <= media < 6.9" quer dizer que a média está entre 5.0 e 6.9, incluíndo o 5.0 no intervalo.
elif 5.0 <= media < 6.9:
    print('RECUPERAÇÃO!!')
