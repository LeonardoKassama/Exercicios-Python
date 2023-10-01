from colorama import init, Fore, Style
init(autoreset=True)

primeiro_valor = int(input(print('Digite um valór qualquer:')))
segundo_valor = int(input(print('Digite outro valór:')))

print('⍊' * 20)
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '''[1]→ Soma
[2]→ Multiplicar
[3]→ Maior
[4]→ Novos números
[5]→ Sair do programa''')
print('⍑' * 20)
resposta = 0
while resposta != 5:
    resposta = int(input(print('Escolha a funcionalidade que desejar')))
    if resposta == 1:
        soma = primeiro_valor + segundo_valor
        print('A soma dos dois números é {}'.format(soma))
    elif resposta == 2:
        produto = primeiro_valor * segundo_valor
        print('O produto dos dois números é {}'.format(produto))
    elif resposta == 3:
        if primeiro_valor > segundo_valor:
            print('Entre os dois números, o {} é o maior e o {} é o menór'.format(primeiro_valor, segundo_valor))
        else:
            print('Entre os dois números, o {} é o maior e o {} é o menór'.format(segundo_valor, primeiro_valor))
    elif resposta == 4:
        primeiro_valor = int(input('Digite um valór qualquer:'))
        segundo_valor = int(input('Digite outro valór'))
print('FIM DO PROGRAMA!')
