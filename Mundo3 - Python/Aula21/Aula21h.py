#ESCOPOS

def teste(parametroB):
    global variavelGlobalA
    variavelGlobalA = 8 # usando o global eu invoco a global e altero ela dentro da função, ela passa a valer 8
    parametroB += 4
    variavelLocalC = 2
    print(f'variavelGlobalA dentro vale {variavelGlobalA}')
    print(f'parametroB dentro vale {parametroB}')
    print(f'variavelLocalC dentro vale {variavelLocalC}')

variavelGlobalA = 5
teste(variavelGlobalA)
print('-' * 30)
print(f'variavelGlobalA dentro vale {variavelGlobalA}')