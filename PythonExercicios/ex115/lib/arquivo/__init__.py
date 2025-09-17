from PythonExercicios.ex115.lib.interface import *

def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') # rt -> read text, vai tentar abrir o arquivo passado no parametro e ler o que está dentro dele
        a.close()
    except FileNotFoundError: #Se o Arquivo não for encontrado.
        return False
    else:
        return True

def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+') #tenta abrir o arquivo como write text, escrever texto e o + serve para que se não existir ele cria o arquivo
        a.close()
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')

def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '') #dados 1 que é a idade tem o \n no final e será substituido por espaço vazio para nao pular linha
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at') #at = append text, ou seja, adicionar coisas ao arquivo
    except:
        print('Houve um erro na abertura arquivo!')
    else:
        try:
            a.write(f'{nome:};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} com sucesso!')
            a.close()

