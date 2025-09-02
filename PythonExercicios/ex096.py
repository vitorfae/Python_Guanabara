def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {resultado}m²')

print(' CONTROLE DE TERRENOS ')
print('-' * 22)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg, compr)
