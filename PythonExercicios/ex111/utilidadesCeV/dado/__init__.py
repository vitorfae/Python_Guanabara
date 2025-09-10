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
            print(f'\033[31mERRO: {valor} e um preco invalido\033[m')