frase = ('Curso em Video Python')

#FATIAMENTO


print(frase[9]) #trazer posição da string.
print(frase[9:13]) #traz o que está escrito da posição 9 a 12.
print(frase[:5]) #traz o que está escrito do inicio até a posição 4
print(frase[9:]) #traz o que está escrito da posição 9 até o final.
print(frase[9::3]) #traz o que está escrito de nove até o final pulando de 3 em 3.
print(frase[9:21:2]) #traz o que está escrito de 9 a 20 e pulando de 2 em 2.
print('')

#ANÁLISE

print(len(frase)) #Vai mostrar o comprimento da frase
print(frase.count('o')) #traz quantas vezes aparece 'o' na frase.
print(frase.count('o',0,13)) #traz quantos 'o' tem entre o inicio e o indice 12
print(frase.find('deo')) #traz em que posição foi encontrado, ou seja, onde inicia.
print(frase.find('android')) #buscar a palavra android na frase, se for falsa retorna -1.
print('Curso' in frase) #retorna true ou false caso a palavra esteja ou não na frase.
print('')

#TRANSFORMAÇÃO

print(frase.replace('Python', 'android')) #Trocar a palavra 'Python' por 'android' apenas na exibição
print(frase.upper()) #Deixar todas as letras maiúsculas
print(frase.lower()) #Deixar todas as letras minusculas
print(frase.capitalize()) #Joga todos os caracteres para minusculos e só o primeiro caractere fica maiusculo.
print(frase.title())  #Vai analisar quantas palavras tem na string e vai deixar maiusculo o inicio de cada palavra.
print('')
frase2 = ('   Aprenda Python  ')
print(frase2)
print(frase2.strip()) #remove os espaços excedentes do início e do fim.
print(frase2.rstrip()) #remove os espaços excedentes apenas do lado direito.
print(frase2.lstrip()) #remove os espaços excedentes apenas do lado esquerdo.
print('')

#DIVISÃO

print(frase.split()) # vai separar a palavra por espaços e indexar por palavras e não letras mais.
print('')

#JUNÇÃO

print('-'.join(frase.split())) #join usado para juntar quando estiver split.