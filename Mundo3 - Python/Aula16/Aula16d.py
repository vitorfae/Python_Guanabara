a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print('')
print(b)
print('')
#junta a tupla 'A' com a tupla 'B'.
print(c)

print('')

#quantidade de itens das tuplas (tamanho)
print(len(c))

print('')

#Quantas vezes aparece o numero 5 na tupla 'C'
print(c.count(5))

print('')

print(c)
#Qual posicao esta o numero 5 (sempre primeira posicao)
print(c.index(5))

print('')

#Caso tenha dois e eu queira mostrar a partir da posicao dele, so precisa colocar virgula e a posicao de inicio
print(c.index(5, 2))
