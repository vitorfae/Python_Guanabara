try: #TENTE -
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resposta = a / b
except: #EXCEÇÃO -
    print('Infelizmente tivemos um problema :(')

else: # SENÃO - caso esteja correto
    print(f'O resultado é {resposta}')

finally:#FINALIZAR - Após terminar todo o try,exceção e o else executa o finally, apos finalizar a tentativa
    print('Volte sempre! Muito obrigado!')


'''
try: #TENTAR -> fica a operação.

except: #EXCEÇÃO -> Caso falhe algo vem para essa claúsula

else: #SENÃO -> Caso der certo na tentativa da operação que está no try. (OPCIONAL de usar)

finally: #FINAL -> Quando finalizado tanto se deu certo ou errado vai executar. (OPCIONAL de usar)



'''
