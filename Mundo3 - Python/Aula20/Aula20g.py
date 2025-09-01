def contador(*num):  # O (* num) o asterisco quer dizer desempacotar e o num é apenas o parametro, ou seja, vai receber vários valores.
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todos {tamanho} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)