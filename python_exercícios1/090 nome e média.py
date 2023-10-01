aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input('Média: '))
if aluno['media'] > 7:
    aluno['situation'] = 'Aprovado'
elif 7 >= aluno['media'] >= 5:
    aluno['situation'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situation'] = 'Reprovado'

print('=-' * 20)

for chave, valor in aluno.items():
    print(f'{chave} é {valor}')
