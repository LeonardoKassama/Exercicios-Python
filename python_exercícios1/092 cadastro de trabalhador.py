from datetime import date
dados = dict()

# recebendo dados do usuário
dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nascimento
carteira = int(input('Carteira de trabalho: (0 to pass) '))
if carteira != 0:
    dados['CTPS'] = carteira
    dados['ano_contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    ano_aposentadoria = dados['ano_contrato'] + 35
    dados['idade_aposentadoria'] = ano_aposentadoria - ano_nascimento
else:
    dados['carteira'] = 'Vazio'

# apresentando os dados
print()
print('⩵' * 20)
for chave, valor in dados.items():
    print(f'-{chave} tem o valor: {valor}')
