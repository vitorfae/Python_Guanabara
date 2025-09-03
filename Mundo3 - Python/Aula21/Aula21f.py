#ESCOPOS

def teste(parametroB):
    parametroB += 4
    variavelLocalC = 2
    print(f'variavelGlobalA dentro vale {variavelGlobalA}')
    print(f'parametroB dentro vale {parametroB}')
    print(f'variavelLocalC dentro vale {variavelLocalC}')

variavelGlobalA = 5
teste(variavelGlobalA)
print('-' * 30)
print(f'variavelGlobalA dentro vale {variavelGlobalA}')
#print(f'parametroB dentro vale {parametroB}') Dão erro por conta de escopo
#print(f'variavelLocalC dentro vale {variavelLocalC}') Dão erro por conta do escopo