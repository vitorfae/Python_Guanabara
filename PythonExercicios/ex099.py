from time import sleep

def maior(* parametros):
    lista = []
    print('-' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for valores in parametros:
        lista.append(valores)
        print(valores, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(parametros)} valores ao todo')
    if sum(lista) == 0:
        maior = 0
    else:
        maior = max(lista)
    print(f'O maior valor informado foi {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#JEITO GUANABARA
'''def maior(* parametros):
    contador = maior = 0
    print('-' * 30)
    print('Analisando os valores passados...')
    for valores in parametros:
        print(f'{valores} ', end='')
        sleep(0.3)
        if contador == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''