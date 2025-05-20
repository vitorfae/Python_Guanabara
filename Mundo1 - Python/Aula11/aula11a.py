#testes
print('\033[41mteste') # letra cor branca, fundo vermelho
print('\033[4;33;44mteste') # letra sublinhada, letra cor amarela, fundo azul
print('\033[1;35;43mteste') # letra em negrito, letra cor roxa, fundo amarelo
print('\033[;42mteste')   # letra cor branca, fundo verde
print('\033[mteste')        # letra e cores padrão
print('\033[7mteste')    # letra negative e cor da letra branca, inverte o fundo

print('\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a, b))
#Após o término da cor desejada, só escrever \033[m -> para finalizar e voltar as cores para o padrão