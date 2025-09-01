def soma(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'A soma dos valores {valores} é {s}')


soma(5, 2)
soma(2, 9, 4)