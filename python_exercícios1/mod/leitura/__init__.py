def leiaInt(mensagem, limit=9999, cor='\x1b[97m'):
    """
    -> Funçõa para validar a entrada de valores inteiros
    :param cor: Define a cor com a qual a mensagem será exibida
    :param limit: limita o valor máximo a ser lido
    :param mensagem: recebe uma string
    :return: retorna um valor inteiro
    """
    limite = limit
    while True:
        try:
            numero = int(input(cor + mensagem))
        except(ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não introduzir os dados!\033[m')
            continue
        if numero > limite:
            print('\033[0;31mErro: Digite uma opção válida!\033[m')
            continue
        else:
            break
    return numero


def leiaFloat(mensagem, limit=9999):
    """
    -> Função para validar a entrada de valores reais
    :param limit: limita o valor máximo a ser lido
    :param mensagem: recebe uma string
    :return: retorna um valor real
    """
    limite = limit
    while True:
        try:
            numero = float(input(mensagem))
        except(ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não introduzir os dados\033[m')
            continue
        if numero > limite:
            print('\033[0;31mErro: Digite uma opção válida!\033[m')
            continue
        else:
            break
    return numero
