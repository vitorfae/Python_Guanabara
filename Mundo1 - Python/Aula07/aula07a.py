nome = input('Qual é seu nome? ') #Camila/ nome exemplo
print('Prazer em te conhecer {:=^20}!'.format(nome))
#print(=*20) - repete o igual 20 vezes
#Saida: ====================

#print(:20) - ocupa 20 caracteres, o que não for preenchido com nome vai ser com espaço vazio
#Saída: Camila              !

#print(:<20) - nome alinhado a esquerda
#saida: Camila              !

#print(:>20) - nome alinhado a direita
#Saida:               Camila!

#print(:^20) - alinhado no centro
#saida:        Camila       !

#print(:=^20) - nome centralizado em 20 espaços com iguais ao lado
#Saida: =======Camila=======!