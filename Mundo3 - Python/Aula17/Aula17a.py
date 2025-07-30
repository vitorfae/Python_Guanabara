#TUPLA DA ERRO POIS É IMUTAVEL
'''
num = (2, 5, 9, 1)
num[2] = 3
print(num)
'''

num = [2, 5, 9, 1]
num[2] = 3 #Adicionando valor 3 na posição 2.
num.append(7) #Adicionando número ao final.
num.insert(1, 0) #Insere o número 0 na posição 1.
num.sort() #Ordena por ordem crescente.
num.pop() # excluí a última posição.
num.pop(2) #excluí o que tem na posição 2.
#num.sort(reverse=True) #Ordena por ordem decrescente.
print(f'Essa lista tem {len(num)} elementos.')
print(num)