print('Digite um número e escolha o tipo de conversão')
numero = int(input('Digite o número aqui: '))
print('='*20)
print('1 - para binário\n2 - para octal\n3 - para hexadecimal')
print('='*20)
conversao = int(input())

if conversao == 1:
    print('O valor {} em binário é {}'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('O valor {} em octal é {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('O valor {} em hexadecimal é {}'.format(numero, hex(numero)[2:])) #[2:] fatiamento de string, para ir do caractere da posição 2 ao final
else:
    print('ERRO! Reinicie o programa')