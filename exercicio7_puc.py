lista_answ = []
arg = True
while arg:
    answ = input('Tipos de problemas'
                 '\n1 - Necessita de esfera'
                 '\n2 - Necessita de limpeza'
                 '\n3 - Necessita de troca de cabo ou conector'
                 '\n4 - quebrado ou inutilizado')
    opc = [1, 2, 3, 4]
    x = answ.isdigit()
    if answ.isdigit():
        answ = int(answ)
        if answ in opc:
            lista_answ.append(answ)
        elif answ == 0:
            print(lista_answ)
            arg = False
    else:
        print('\nValor invalido, tente novamente!!!!')

