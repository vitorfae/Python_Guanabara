from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('opção 1')
    elif resposta == 2:
        cabecalho('opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção inválida\033[m')
    sleep(2)









'''print('-'*30)
print('MENU PRINCIPAL'.center(30))
print('-'*30)
print('\033[033m1 -\033[m', end=' ')
print('\033[034mVer pessoas cadastradas')
print('\033[033m2 -\033[m', end=' ')
print('\033[034mCadastrar nova pessoa')
print('\033[033m3 -\033[m', end=' ')
print('\033[034mSair do sistema')

opcao = int(input('Sua Opção: '))'''