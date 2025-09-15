def leiaInt(numero):
    while True:
        try:
            inteiro = int(input(numero))
        except KeyboardInterrupt:
            print('\n\033[031mO usuário prefiriu não digitar esse número\033[m')
            return 0

        except:
            print('\033[031mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return inteiro

def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao