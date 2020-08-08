def calcular(valor):
    comissao = valor*0.09
    salario = 200 + comissao
    return salario

lista_resultados = []
arg = True
while arg:
    vendas = int(input('valor total das vendas realizadas?'))
    if vendas!=0:
        salario = calcular(vendas)
        lista_resultados.append(salario)
        print(lista_resultados)
    else:
        arg = False