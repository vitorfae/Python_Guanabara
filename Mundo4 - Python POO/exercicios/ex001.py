#Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método construtor
        #Atributos de instância
        self.nome = ""  #Self é um nome genérico de um atributo de instância, ou seja, na execução troca o self pelo chamador, ou seja, self muda para gafanhoto1 ou gafanhoto2, depende o qual está chamando.
        self.idade = 0

    #Métodos de instância
    def aniversario(self):
        #self.idade = self.idade + 1  
        self.idade += 1 #Self é um nome genérico de um atributo de instância, ou seja, na execução troca o self pelo chamador, ou seja, self muda para gafanhoto1 ou gafanhoto2, depende o qual está chamando.

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    
#Declaração de Objetos
gafanhoto1 = Gafanhoto()             #Instanciando objeto
print(gafanhoto1.mensagem())         #printando objeto vazio, pois não foi passado atributos
gafanhoto1.nome = "Vitor"            #passando atributos
gafanhoto1.idade = 21                #passando atributos
print(gafanhoto1.mensagem())         #printando objeto já com valores atribuídos
gafanhoto1.aniversario()             #chamando o método aniversário onde vai somar mais 1 na idade
print(gafanhoto1.mensagem())         #printando objeto, após execução do método aniversário.

#2º objeto
gafanhoto2 = Gafanhoto()
gafanhoto2.nome = "Mauro"
gafanhoto2.idade = 53
print(gafanhoto2.mensagem())

gafanhoto3 = Gafanhoto()
print(gafanhoto3.mensagem())