from colorama import init, Fore, Style, Back
init(autoreset=True)

termos_exibidos = 0
numero_de_termos = 10
# nome do programa.
print(Back.LIGHTYELLOW_EX + Fore.LIGHTBLACK_EX + Style.BRIGHT + '{:🀰^33}'.format(' ⚛︎ GERADOR DE PA ⚛︎ '))
# introdução dos dados iniciais
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
# calculando a posição do termo
posicao_do_termo = primeiro_termo + (numero_de_termos - 1) * razao

termo_anterior = primeiro_termo

while numero_de_termos != 0:
    for i in range(termo_anterior, posicao_do_termo + 1, razao):
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '{}'.format(i), end=' → ')
        termos_exibidos += 1
        termo_anterior += razao
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + 'Pausa...')
    novo_numero_de_termos = int(input(Fore.BLUE + 'Quantos termos mais desejas mostrar? '))
    # para que a condição do loop acima possa ser falsa,
    # atribuimos o valor do "novo_numero_de_termos" à variavel "numero_de_termos".
    numero_de_termos = novo_numero_de_termos
    posicao_do_termo = termo_anterior + (novo_numero_de_termos - 1) * razao
print('Foram exibidos {} termos.'.format(termos_exibidos))
print(Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + '{: ^39}'.format('︎! FIM DO PROGRAMA !'))
