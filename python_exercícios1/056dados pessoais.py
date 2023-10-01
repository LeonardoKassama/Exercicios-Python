# recolher dados de 4 pessoas;
# mostrar:
# média de idade do grupo;
# qual o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.
soma = 0
maisVelho = 0
nomeV = ''
contador = 0
for i in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(i))).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    soma += idade
    if i == 1 and sexo == 'M':
        maisVelho = idade
        nomeV = nome
    elif sexo == 'M' and idade > maisVelho:
        maisVelho = idade
        nomeV = nome
    elif sexo == 'F' and idade < 20:
        contador += 1
media = soma / 4
print('Média da idade do grupo: {}'.format(media))
print('Mulheres com menos de 20 anos: {}'.format(contador))
print('O homem mais velho se chama {}, e tem {} anos.'.format(nomeV, maisVelho))