import datetime

print('Programa sobre alistamento militar')
alistamento = int(18)
anoAtual = int(datetime.date.today().year)
nascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - nascimento

if idade < 18:
    print('Ainda falta {} anos para se alistar'.format(alistamento - idade))
elif idade > 18:
    print('Já passou {} anos do prazo de alistamento'.format(idade - alistamento))
else:
    print('Está na hora de se alistar')