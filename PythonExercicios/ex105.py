def notas(*valores, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param valores:  uma ou mais notas dos alunos (aceita vários)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    resultado = dict()
    #Total de notas digitadas
    totNotas = len(valores)
    resultado['total'] = totNotas
    #Maior nota tirada
    resultado['maior'] = max(valores)
    #Menor nota tirada
    resultado['menor'] = min(valores)
    #Média final do aluno
    resultado['media'] = float(f'{sum(valores) / totNotas:.1f}')
    if situacao is False:
        return resultado
    else:
        if situacao is True:
            if resultado['media'] >= 7:
                resultado['situacao'] = 'BOA'
            elif resultado['media'] < 7 and resultado['media'] > 4:
                resultado['situacao'] = 'RAZOAVEL'
            elif resultado['media'] <= 4:
                resultado['situacao'] = 'RUIM'
        return  resultado


resp = notas(3.5, 10, 6.5, situacao=True)
print(resp)
help(notas)


#JEITO GUANABARA
'''def notas(*numeros, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param valores:  uma ou mais notas dos alunos (aceita vários)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    resposta = dict()
    resposta['total'] = len(numeros)
    resposta['maior'] = max(numeros)
    resposta['menor'] = min(numeros)
    resposta['media'] = sum(numeros)/len(numeros)
    if situacao:
        if resposta['media'] >= 7:
            resposta['situacao'] = 'BOA'
        elif resposta['media'] >= 5:
            resposta['situacao'] = 'RAZOAVEL'
        else:
            resposta['situacao'] = 'RUIM'
    return resposta




#Programa principal
resp = notas(5.5, 2.5, 9, 8.5, situacao=True)
print(resp)
print(help(notas))
'''