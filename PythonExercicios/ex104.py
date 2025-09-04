def leiaInt(numero):
    #print(numero) # exibe apenas a mensagem
    valor = input(numero) #faz um input com a mensagem Digite um número exibido na linha 11, passa o texto como parametro, ou seja, input da frase passada como parametro
    while valor.isnumeric() is False: #Enquanto o valor.isnumeric for falso, ou seja enquanto não for número ele roda o for
        print('\033[031mERRO! Digite um número inteiro válido.\033[m')
        valor = input(numero)
    return valor


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')