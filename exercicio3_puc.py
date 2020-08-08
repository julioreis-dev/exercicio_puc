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


def analisar(voto, total):
    lista_resultado = []
    index = 0
    for n in voto:
        percentual = (n*100)/total
        index = index + 1
        resulta_parcial = (percentual, index, n)
        lista_resultado.append(resulta_parcial)
    return lista_resultado


def votar():
    lista_voto = []
    arg = True
    while arg:
        opcao = int(input('Número do jogador (0=fim)?'))
        if opcao in range(1, 24):
            lista_voto.append(opcao)
            pass
        elif opcao == 0:
            arg = False
        else:
            print('\nOption not available, try again!!!\n')
    return lista_voto


print('Enquete: Quem foi o melhor jogador?')
votacao = votar()
votacao_jogador = computar(votacao)
total_votos = apurar(votacao_jogador)
x = sorted(analisar(votacao_jogador, total_votos), reverse=True)
print(x)
print('resultado da votação:'
      f'\nForam computados {total_votos} votos.\n'
      f'Jogador  Votos        %\n'
      f'{x[0][1]}       {x[0][2]}      {x[0][0]}\n'
      f'{x[1][1]}       {x[1][2]}      {x[1][0]}\n'
      f'{x[2][1]}       {x[2][2]}      {x[2][0]}\n'
      f'\nO melhor jogador foi o número {x[0][1]}, com {x[0][2]} votos, correspondendo a {x[0][0]}% do total de votos.')
