def contador(* num): #O (* num) o asterisco quer dizer desempacotar e o num é apenas o parametro, ou seja, vai receber vários valores.
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)