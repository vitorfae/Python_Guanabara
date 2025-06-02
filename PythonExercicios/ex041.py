from datetime import date

print('Calculo de categoria segundo a Confederação Nacional de Natação')
anoNascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = date.today().year
idadeAtual = anoAtual - anoNascimento

if idadeAtual <= 9:
    print('Sua categoria é MIRIM')
elif idadeAtual <= 14:
    print('Sua categoria é INFANTIL')
elif idadeAtual <= 19:
    print('Sua categoria é JUNIOR')
elif idadeAtual <= 20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')