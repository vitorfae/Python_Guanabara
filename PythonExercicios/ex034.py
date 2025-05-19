salario = float(input('Digite o salário: '))
if salario >= 1250.00:
    salario *= 1.1
    print('O novo salário é R${:.2f}'.format(salario))
else:
    salario *= 1.15
    print('O novo salário é R${:.2f}'.format(salario))