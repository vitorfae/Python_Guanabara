#VÁRIAVEIS COMPOSTAS
'''
TUPLAS -> ()
LISTA -> []
DICIONARIO -> {}
'''

#Tuplas - Tuplas sao IMUTAVEIS
'''
No novo python pose ser criado tuplas sem os parenteses.
EXEMPLO: lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print('')
print(lanche[-2]) #quando tem negativo vem de traz para frente = saida: Pizza
print('')
print(lanche[1:3]) # vai mostrar do elemento 1 ao 2, pois desconsidera o ultimo
print('')
print(lanche[2:]) # vai da pizza ate o final
print('')
print(lanche[:2]) # hamburguer ate suco, o ultimo elemento nao conta
print('')
print(lanche[-2:]) # pizza e vai ate o final
print('')
print(lanche)
print('')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('')
print(len(lanche)) #Vai contar quantos indices tem na tupla lanche