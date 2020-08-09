def calcular(lista, tot, num):
    lista_resultado = []
    repetidos = lista.count(num)
    percentual = (repetidos*100)/tot
    lista_resultado.append(repetidos)
    lista_resultado.append(percentual)
    return lista_resultado


lista_answ = []
arg = True
while arg:
    answ = input('\nTipos de problemas'
                 '\n1 - Necessita de esfera'
                 '\n2 - Necessita de limpeza'
                 '\n3 - Necessita de troca de cabo ou conector'
                 '\n4 - quebrado ou inutilizado '
                 '\n')
    opc = [1, 2, 3, 4]
    if answ.isdigit():
        answ = int(answ)
        if answ in opc:
            lista_answ.append(answ)
            arg = True
        elif answ == 0:
            print(lista_answ)
            total = len(lista_answ)
            print(f'\nQuantidades de mouses: {total}'
                  f'\nSituação                                   Quantidade    Percentual'
                  f'\n1-Necessita de esfera                         {calcular(lista_answ, total, 1)[0]}            {calcular(lista_answ, total, 1)[1]}%'
                  f'\n2-Necessita de limpeza                        {calcular(lista_answ, total, 2)[0]}            {calcular(lista_answ, total, 2)[1]}%'
                  f'\n3-Necessita de troca de cabo ou conector      {calcular(lista_answ, total, 3)[0]}            {calcular(lista_answ, total, 3)[1]}%'
                  f'\n4-quebrado ou inutilizado                     {calcular(lista_answ, total, 4)[0]}            {calcular(lista_answ, total, 4)[1]}%')

            arg = False
        else:
            print('Opçãp inválida')
    else:
        print('\nValor invalido, tente novamente!!!!')
