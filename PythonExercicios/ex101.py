from datetime import date

def voto(ano = 0):
    anoAtual = date.today().year
    if ano <= 0:
        ano = anoAtual

    idade = anoAtual - ano
    if idade < 18:
        return idade, 'NAO VOTA'
    elif idade >= 18 and idade <= 65 :
        return idade, 'VOTO OBRIGATORIO'
    else:
        return idade, 'VOTO OPCIONAL'


print('-' * 30)
anoNascimento = int(input('Em que ano voce nasceu? '))
resposta = voto(anoNascimento)
print(f'Com {resposta[0]} anos: {resposta[1]}.')

#OUTRA MANEIRA

def votar(anonasc = 0 ):
    anoAtual = date.today().year
    if anonasc <= 0:
        anonasc = anoAtual
    idade = anoAtual - anonasc
    if idade < 18:
        return (f'Com {idade} anos: NAO VOTA.')
    elif idade >= 18 and idade <= 65 :
        return (f'Com {idade} anos: VOTO OBRIGATORIO.')
    else:
        return (f'Com {idade} anos: VOTO OPCIONAL.')

print('-=' * 15)
anonasc = int(input('Em que ano voce nasceu? '))
resultado = votar(anonasc)
print(resultado)