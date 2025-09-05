def votar(anonasc = 0 ):
    from datetime import date
    anoAtual = date.today().year
    if anonasc <= 0:
        anonasc = anoAtual
    idade = anoAtual - anonasc
    if idade < 16:
        return (f'Com {idade} anos: NAO VOTA.')
    elif idade >= 18 and idade <= 65 :
        return (f'Com {idade} anos: VOTO OBRIGATORIO.')
    elif 16 <= idade < 18 or idade >= 65:
        return (f'Com {idade} anos: VOTO OPCIONAL.')


anonascimento = int(input('Em que ano voce nasceu? '))
resultado = votar(anonascimento)
print(resultado)

#OUTRA MANEIRA

'''def voto(ano = 0):
    from datetime import date
    anoAtual = date.today().year
    if ano <= 0:
        ano = anoAtual

    idade = anoAtual - ano
    if idade < 16:
        return idade, 'NAO VOTA'
    elif idade >= 18 and idade <= 65 :
        return idade, 'VOTO OBRIGATORIO'
    elif 16 <= idade < 18 or idade >= 65:
        return idade, 'VOTO OPCIONAL'


print('-' * 30)
anoNascimento = int(input('Em que ano voce nasceu? '))
resposta = voto(anoNascimento)
print(f'Com {resposta[0]} anos: {resposta[1]}.')'''