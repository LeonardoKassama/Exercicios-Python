from mod.exibição import titulo
from time import sleep

def arquivoExiste(nome):
    """
    -> Função que verifica se um arquivo existe ou não
    :param nome: nome do arquivo a ser verificado
    :return: um valor boleano
    """
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    -> Função que cria um arquivo "nome"
    :param nome: Define o nome do arquivo a ser criado
    :return: Sem retorno
    """
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print(f'Ouve um erro na criaçã do arquivo {nome}')
    else:
        print(f'O arquivo \033[34m{nome}\033[m foi criado com sucesso')


def lerArquivo(nome):
    """
    -> Função para ler o arquivo "nome"
    :param nome: Define o arquivo a ser lido
    :return: Sem retorno
    """
    try:
        arquivo = open(nome, 'rt')
    except:
        print(f'Erro ao ler o arquivo {nome}')
    else:
        sleep(2)
        titulo('pessoas cadastradas', borda=13)
        print(arquivo.read())
        arquivo.close()


def escreverArquivo(arquivo, nome='desconhecido', idade=0):
    """
    -> Função para escrever dados no arquivo "nome"
    :param arquivo: Define o nome do arquivo em que os dados serão escritos
    :param nome: Define um dos dados a serem escritos
    :param idade: Define um dos dados a serem escritos
    :return: Sem retorno
    """
    try:
        arquivo = open(arquivo, 'a')
    except:
        print(f'Erro ao abrir o arquivo!')
    else:
        # faz todo o tratamento necessario no nome
        nome_final = ' '.join(nome.strip().title().split())
        medida = 40 - len(nome_final)
        arquivo.writelines(f'{nome_final}{idade:>{medida}} anos\n')
        sleep(1)
        print(f'Novo registro de {nome_final} adicionado.')
        arquivo.close()
