from colorama import Back as B, Style as S, Fore as F, init
init(autoreset=True)

homens = mulheres = m_comMenosDe20Anos = pessoas_maiores = 0
print(F.LIGHTYELLOW_EX + S.BRIGHT + B.LIGHTWHITE_EX + '{:^40}\033[m'.format('PROGRAMA CADASTRO ESTATÍSTICO'))
print(B.LIGHTWHITE_EX + '                   📈                   ')

while True:
    print(S.BRIGHT + F.LIGHTBLUE_EX + '\n\033[4m{:^40}'.format('CADASTRE UMA PESSOA'))
    idade = int(input('Digite a sua idade: '))
    # validando o sexo:
    sexo = str(input('Qual o seu sexo [\033[1;34m{}\033[m/\033[1;35m{}\033[m]: '
                     .format('M', 'F'))).upper().strip()[0]
    while sexo not in 'MF':
        print(F.LIGHTWHITE_EX + S.BRIGHT + B.LIGHTRED_EX + '{:^40}'.format('OPÇÃO INVÁLIDA!'))
        sexo = str(input("Qual o seu sexo [\033[1;34m{}\033[m/\033[1;35m{}\033[m]: "
                         .format('M', 'F'))).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    else:
        mulheres += 1
        # verificando mulheres com menos de 20 anos:
        if idade < 20:
            m_comMenosDe20Anos += 1
    # verificando pessoas com mais de 18 anos:
    if idade > 18:
        pessoas_maiores += 1
    # perguntando se o usuário deseja ou não continuar. E validando a resposta:
    continuar = str(input('Deseja continuar? [\033[1;32m{}\033[m/\033[1;31m{}\033[m]: '
                          .format('S', 'N'))).upper().strip()[0]
    while continuar not in 'SN':
        print(F.LIGHTWHITE_EX + S.BRIGHT + B.LIGHTRED_EX + '{:^40}'.format('OPÇÃO INVÁLIDA!'))
        continuar = str(input('Deseja continuar? [\033[1;32m{}\033[m/\033[1;31m{}\033[m]: '
                              .format('S', 'N'))).upper().strip()[0]
    if continuar == 'N':
        break
# exibindo as estatísticas:
print('\n')
print(B.LIGHTWHITE_EX + S.BRIGHT + F.CYAN + '\033[4m{:^38}'.format('📊 ESTATÍSTICAS 📈'))
print('⁃' * 40)
print(f'''➤ Pessoas maiores de +18: \033[1;36m{pessoas_maiores}\033[m
➤ Número de homens cadastrados: \033[1;36m{homens}\033[m
➤ Número de mulheres com menos de 20 anos: \033[1;36m{m_comMenosDe20Anos}''')
print('⁃' * 40)
