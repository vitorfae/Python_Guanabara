lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#Caso nao precisa de posicao
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('')

#Caso precise da posicao usando range
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posicao {contador}')
print('Comi pra caramba')

print('')

#tras posicao e item
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba')