def titulo(string, cor = '\x1b[97m', borda=8):
    """
    -> cria a exibição de um título ajustavel com a cor definida
    :param borda: define o espaço a ser deixado nas bordas
    :param string: a string a ser exibida
    :param cor: uma cor da biblioteca colorama
    :return: sem retorno
    """
    from colorama import Style, init
    init(autoreset=True)
    def centro():
        return len(string) + borda * 2
    print('-'* centro())
    print(Style.BRIGHT + cor + f'{string.upper():^{centro()}}')
    print('-' * centro())

def menu(etiqueta, *options, borda):
    """
    -> Função para a exibição de menus
    :param etiqueta: Define o título do menu
    :param options: Define a lista de itens do menu
    :param borda: Define o espaço a ser deixado nas bordas
    :return: Sem retorno
    """
    from colorama import init
    init(autoreset=True)
    titulo(etiqueta, borda=borda)

    # iterando nos elementos da tupla "options"
    # disponibilisando assim as opções do menú na tela
    for indice,option in enumerate(options):
        print(f'\033[1;33m{indice+1}\033[m - \033[1;36m{option.title()}')

    # obtendo o comprimento total das barras limitantes do menu
    comprimento = len(etiqueta.upper()) + (2*borda)
    print('-' * comprimento)
