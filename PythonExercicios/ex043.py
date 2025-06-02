from time import sleep

print('='*18)
print('CALCULADORA DE IMC')
print('='*18)
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('CALCULANDO...')
sleep(3)
if imc < 18.5:
    print('Abaixo do peso!')
    print('Seu IMC é de {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
    print('Seu IMC é de {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
    print('Seu IMC é de {:.2f}'.format(imc))
elif imc >=30 and imc < 40:
    print('Obesidade!')
    print('Seu IMC é de {:.2f}'.format(imc))
else:
    print('Obesidade mórbida!')
    print('Seu IMC é de {:.2f}'.format(imc))