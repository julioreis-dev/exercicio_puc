def calcular(valor):
    comissao = valor * 0.09
    sal = 200 + comissao
    return sal


def catalogar(lista):
    listagem = []
    for n in lista:
        inteiro = n // 100
        listagem.append(inteiro)
    return listagem


lista_resultados = []
arg = True
while arg:
    vendas = int(input('valor total das vendas realizadas?'))
    if vendas != 0:
        salario = calcular(vendas)
        lista_resultados.append(salario)
    else:
        arg = False


def maiores_salario(lista_1):
    contador = 0
    for n in lista_1:
        if n >= 10:
            contador = contador + 1
    return contador


x = catalogar(lista_resultados)
print(f'temos {x.count(2)} com salario entre R$200 - R$299'
      f'\ntemos {x.count(3)} com salario entre R$300 - R$399'
      f'\ntemos {x.count(4)} com salario entre R$400 - R$499'
      f'\ntemos {x.count(5)} com salario entre R$500 - R$599'
      f'\ntemos {x.count(6)} com salario entre R$600 - R$699'
      f'\ntemos {x.count(7)} com salario entre R$700 - R$799'
      f'\ntemos {x.count(8)} com salario entre R$800 - R$899'
      f'\ntemos {x.count(9)} com salario entre R$900 - R$999'
      f'\ntemos {maiores_salario(x)} com salario entre R$1000 em diante')
