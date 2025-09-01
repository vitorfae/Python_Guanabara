def contador(inicio, fim, passo):
    print('-' * 30)
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        if passo < 0:
            passo *= -1
        for valor in range(inicio, fim + 1, passo):
            print(valor, end=' ')
        print('FIM!')
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        if passo > 0:
            passo *= -1
        for valor in range(inicio, fim - 1, passo):
            print(valor, end=' ')
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
