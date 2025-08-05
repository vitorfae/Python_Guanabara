valores = []

for c in range(0, 5):
    digitado = int(input('Digite um valor: '))
    if c == 0:
        valores.append(digitado)
        print('Adicionado ao final da lista')
        print(valores)
    else:
        for cont in range(0, len(valores)):
            if digitado < valores[cont] and digitado not in valores:
                valores.insert(cont, digitado)
            elif digitado > valores[cont] and digitado not in valores:
                valores.append(digitado)

        print(valores)


