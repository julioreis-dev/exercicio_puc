def computar(list_votos):
    lista_total = []
    for n in range(1, 24):
        repet = list_votos.count(n)
        lista_total.append(repet)
    return lista_total

def apurar(list_soma):
    soma = 0
    for n in list_soma:
        soma = soma + n
    return soma

lista_voto = []
arg = True
while arg:
    print('Quem foi o melhor jogador?\n')
    opcao = int(input('Número do jogador (0=fim)?'))
    if opcao in range(1, 24):
        lista_voto.append(opcao)
        pass
    elif opcao == 0:
        x = computar(lista_voto)
        y = apurar(x)
        print(y)
        arg = False
    else:
        print('\nOption not available, try again!!!\n')
