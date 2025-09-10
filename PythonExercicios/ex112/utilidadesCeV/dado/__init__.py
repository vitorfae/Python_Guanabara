def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip()
        if valor.isnumeric():
            valor = int(valor)
            return valor
            break
        elif ',' in valor or '.' in valor:
            valor = valor.replace(',', '.')
            valor = float(valor)
            return valor
            break
        else:
            print(f'\033[31mERRO: "{valor}" e um preco invalido\033[m')


#JEITO GUANABARA

'''def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" e um preco invalido\033[m')
        else:
            valido = True
            return float(entrada)''' #mas da erro quando for alfa numerico