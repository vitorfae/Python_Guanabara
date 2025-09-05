from time import sleep

def titulos(msg):
    if msg == cabecalho:
        print('\033[;42m', end='')
    elif msg == manual:
        print('\033[44m', end='')
    else:
        print('\033[41m', end='')

    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4),)
    print('\033[m', end='')
    sleep(1)

def pesquisar(valor):
    print('\033[30;47m', end='')
    return help(valor)


#Programa principal
while True:
    cabecalho = 'SISTEMA DE AJUDA PyHELP'
    titulos(cabecalho)
    ajuda = str(input('Função ou Biblioteca > '))
    if ajuda.upper() == 'FIM':
        fim = 'ATÉ LOGO!'
        titulos(fim)
        break
    manual = f"Acessando o manual do comando '{ajuda}'"
    titulos(manual)
    pesquisar(ajuda)
    sleep(2)


#JEITO GUANABARA
'''cores = ('\033[m',        # 0 - sem cores
         '\033[0;30;41m', # 1- vermelho
         '\033[0;30;42m', # 2- verde
         '\033[0;30;43m', # 3- amarelo
         '\033[0;30;44m', # 4- azul
         '\033[0;30;45m', # 5- roxo
         '\033[0;30;46m', # 6- azul claro
         '\033[0;30;47m'  # 7- branco
        );


def ajuda(com):
    titulos(f'Acessando o manual do comando "{com}"', 4)
    print(cores[7], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)

def titulos(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulos('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulos('ATÉ LOGO!', 1)'''