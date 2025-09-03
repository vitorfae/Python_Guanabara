#ESCOPOS

def teste(parametroB):
    variavelGlobalA = 8 # vai criar uma variavel local com o mesmo nome, mas com o valor 8
    parametroB += 4
    variavelLocalC = 2
    print(f'variavelGlobalA dentro vale {variavelGlobalA}')
    print(f'parametroB dentro vale {parametroB}')
    print(f'variavelLocalC dentro vale {variavelLocalC}')

variavelGlobalA = 5
teste(variavelGlobalA)
print('-' * 30)
print(f'variavelGlobalA dentro vale {variavelGlobalA}')
#print(f'parametroB dentro vale {parametroB}')
#print(f'variavelLocalC dentro vale {variavelLocalC}')

print()
print('-' * 30)
def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
funcao()
print(f'n1 fora vale {n1}')