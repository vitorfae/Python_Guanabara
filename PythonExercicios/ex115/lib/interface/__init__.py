def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())