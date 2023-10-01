
sexo_da_pessoa = str(input('Informe seu sexo: [M/F]')).upper()

while sexo_da_pessoa not in 'FM':
    sexo_da_pessoa = str(input('Opção inválida!\nPor favor informe seu sexo:')).upper

print('Sexo {} registrado com sucesso!'.format(sexo_da_pessoa))
