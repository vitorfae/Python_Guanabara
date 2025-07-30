num = [2, 5, 9, 1]
num[2] = 3 #Adicionando valor 3 na posição 2.
num.append(7) #Adicionando número ao final.
num.sort(reverse=True) #Ordena por ordem decrescente.
num.insert(2, 2) #Insere o número 2 na posição 2.
'''num.remove(4)''' #Como não tem quatro vai dar um erro. Fazer da maneira a baixo em caso de dúvida
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos.')
print(num)