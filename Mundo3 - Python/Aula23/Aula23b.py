try: #TENTE -
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resposta = a / b
except Exception as erro: #EXCEÇÃO -
    print(f'Infelizmente tivemos um problema :( - O problema encontrado foi {erro.__class__}')

else: # SENÃO - caso esteja correto
    print(f'O resultado é {resposta}')

finally:#FINALIZAR - Após terminar todo o try,exceção e o else executa o finally, apos finalizar a tentativa
    print('Volte sempre! Muito obrigado!')