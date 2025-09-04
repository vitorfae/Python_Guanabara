def notas(*valores, situacao=False):
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


resp = notas(5.5, 4, 4, 2, situacao=True)
print(resp)