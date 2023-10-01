from mod.exibição import menu
from mod.leitura import leiaInt
from mod.arquivo import*

while True:
     # nome do arquivo
     arquivo = 'pessoas_cadastradas.txt'

     # verificando se existe um arquivo e criando-o se ñ for o caso
     if not arquivoExiste(arquivo):
          criarArquivo(arquivo)

     # menu principal
     menu('menu principal',
          'Ver pessoas cadastradas',
          'Cadastrar nova pessoa',
          'Sair do sistema',
          borda=16)

     option = leiaInt('Sua opção: ', limit=3, cor='\033[35m')

     # primeira opção
     if option == 1:
          lerArquivo(arquivo)
          continue

     # segunda opção
     elif option == 2:
          titulo('cadastra uma nova pessoa', borda=11)
          nome = str(input('Nome: '))
          idade = int(input('Idade: '))
          escreverArquivo(arquivo, nome, idade )
          sleep(1)
          continue

     # ultima opção
     elif option == 3:
          break

print('Fim do programa!')
