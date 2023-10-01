from colorama import Fore as F, Back as B
def titulo(string, cor = '\x1b[97m', back = '\033[46m'):
    """
    -> cria a exibição de um título ajustavel com a cor definida
    :param back: cor para o fundo
    :param string: a string a ser exibida
    :param cor: uma cor da biblioteca colorama
    :return: sem retorno
    """
    from colorama import Style, init, Back
    init(autoreset=True)
    def centro():
        return len(string) + 8
    print(back + Style.BRIGHT + '-'* centro())
    print(back + cor + Style.BRIGHT + f'{string.upper():^{centro()}}')
    print(back + Style.BRIGHT + '-' * centro())


def ajuda(comando, back = '\033[40m'):
    titulo(f'Acessando a Documentação de {comando}')
    return f'{help(comando)}'


while True:
    titulo(f'SISTEMA DE AJUDA PyHelp', back=B.GREEN)
    resposta = str(input('Função ou Biblioteca > '))
    if resposta.capitalize() == 'Fim':
        break
    ajuda(resposta, back=B.LIGHTWHITE_EX)
