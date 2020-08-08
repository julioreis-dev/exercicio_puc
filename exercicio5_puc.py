#1-inserir salario. 0 saindo do programa
#2-calcular abono de 20% sobre o salario
#3-apresentar salario e abono
#4-apresentar resumo

def calcular(lista):
    lista_calculada = []
    for salario in lista:
        abono = salario*0.20
        if abono < 100:
            abono = float(100)
            tupla_valores = (salario, abono)
        else:
            tupla_valores = (salario, abono)
        lista_calculada.append(tupla_valores)
    return sorted(lista_calculada, reverse=True)


def calcular_abono(lista_abono):
    somatorio_abono = 0
    for abono in lista_abono:
        somatorio_abono = somatorio_abono + abono[1]
    return somatorio_abono


def calcular_minimo(lista_abono2):
    lista_minimo = []
    for abono2 in lista_abono2:
        abonos = abono2[1]
        lista_minimo.append(abonos)
    valor_minimo = lista_minimo.count(100)
    return valor_minimo


def formatar_dados(lista, abono, minimo):
    print('\nProjeção de Gastos com Abono'
          '\n============================')
    for n in lista:
        print('Salário: {}'.format(n[0]))

    print('\nSalário  -  Abono')
    for i in lista:
        print('R${} - R${}'.format(i[0], i[1]))

    maior_abono = lista
    print(f'\nForam processados {len(lista)} colaboradores'
          f'\nTotal gasto com abonos:R$ {abono}'
          f'\nValor mínimo pago a {minimo} colaboradores'
          f'\nMaior valor de abono pago: R${maior_abono[0][0]}')

arg = True
lista_sal = []
while arg:
    sal = float(input('Digite o salário '))
    if sal != 0:
        lista_sal.append(sal)
    else:
        valores = calcular(lista_sal)
        print(valores)
        total_abono = calcular_abono(valores)
        total_minimo = calcular_minimo(valores)
        formatar_dados(valores, total_abono, total_minimo)
        arg = False


