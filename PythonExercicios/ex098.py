from time import sleep

def contador(inicio, fim, passo):
    print('-' * 30)
    #Ordem crescente
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        sleep(0.7)
        for valor in range(inicio, fim + 1, passo):
            print(valor, end=' ')
            sleep(0.5)
        print('FIM!')
    #Ordem decrescente
    elif inicio > fim:
        if passo == 0:
            passo = -1
        elif passo > 0:
            passo *= -1
        print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}')
        sleep(0.7)
        for valor in range(inicio, fim - 1, passo):
            print(valor, end=' ')
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print(f'Agora é a sua vez de personalizar a contagem!')
inicial = int(input('Início: '))
final = int(input('Fim: '))
pular = int(input('Passo: '))
contador(inicial, final, pular)


#JEITO GUANABARA
'''def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    print('-' * 40)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(0.7)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print(f'Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''