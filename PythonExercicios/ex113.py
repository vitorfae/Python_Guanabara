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


def leiaFloat(num):
    while True:
        try:
            numReal = float(input(num))
        except KeyboardInterrupt:
            print('\n\033[021mEntrada de dados interrompida pelo usuário')
            return 0
        except:
            print('\033[031mERRO: por favor, digite um número real válido.\033[m')
        else:
            return numReal


# Programa principal
numeroInteiro = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numeroInteiro} e o real é {numeroReal}')


'''#PRIMEIRA TENTATIVA
    def leiaInt(numero):
        while True:
            try:
                inteiro = int(input(numero))
            except KeyboardInterrupt:
                inteiro = 0
                return inteiro
                break
            except:
                print('\033[031mERRO: por favor, digite um número inteiro válido.\033[m')
            else:
                return inteiro
                break

def leiaFloat(num):
    while True:
        try:
            numReal = float(input(num))
        except KeyboardInterrupt:
            numReal = 0
            return numReal
            break
        except:
            print('\033[031mERRO: por favor, digite um número real válido.\033[m')
        else:
            return numReal
            break



#Programa principal
numeroInteiro = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numeroInteiro} e o real é {numeroReal}')
'''