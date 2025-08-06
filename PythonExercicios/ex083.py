lista = []
digitado = str(input('Digite um valor: '))
for contador in range(0, len(digitado)):
    lista.append(str(digitado[contador]))

# analisando quantidade de parenteses
aberto = lista.count('(')
fechado = lista.count(')')
if aberto == fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')

#Usei para validação de resultados do array
'''print(len(digitado))
print(digitado)
print(lista)
print(aberto)'''

#JEITO GUANABARA
'''expressao = str(input('Digite uma expressao: '))
pilha = []
for caracter in expressao:
    if caracter == '(': # se tiver parenteses aberto em expressao ele vai adicionar na pilha
        pilha.append('(')
    elif caracter == ')': #Senão se tiver o parenteses fechando ele vai ver se o tamanho da pilha é maior que 0
        if len(pilha) > 0: #Como ele grava só os abertos, o fechado serve apenas para confirmar e remover o aberto certo
            pilha.pop() #sendo assim após ele verificar que tem um parenteses fechado no input e já tem um aberto na lista ele remove o aberto na lista pois ele fecha corretamente
        else:
            pilha.append(')') #senão ele grava apenas o fechado o que vai dar erro, pois falta algo
if len(pilha) > 0:
    print('Sua expressão está está valida') # Se pilha estiver vazia está correto
else:
    print('Sua expressão está errada') # se tiver parenteses aberto ou fechado, vai dar erro, pois tem parenteses a mais'''

