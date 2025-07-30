num = [2, 5, 9, 1]
num[2] = 3 #Adicionando valor 3 na posição 2.
num.append(7) #Adicionando número ao final.
num.sort(reverse=True) #Ordena por ordem decrescente.
num.insert(2, 2) #Insere o número 2 na posição 2.
num.remove(2) #Remove a primeira ocorrência encontrada, ou seja, o primeiro valor 2 da lista
print(f'Essa lista tem {len(num)} elementos.')
print(num)