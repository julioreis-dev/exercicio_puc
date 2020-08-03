def apurar_votos(apurados):
    lista_geral = []
    somatorio = 0
    for valor in apurados:
        somatorio = valor + somatorio

    index = [0, 1, 2, 3, 4, 5]
    for indice in index:
        voto_sistema = apurados[indice]
        percentual = definir_percental(voto_sistema, somatorio,)
        tupla_resultado = (voto_sistema, percentual, somatorio)
        lista_geral.append(tupla_resultado)

    return lista_geral


def definir_percental(valor1, total):
    perc = (valor1 * 100) / total
    return perc

def mostrar_resultado(tupla_dados):
    print('Sistema operacional  Votos  %\n------------------------------------'
          f'\nWindows Server         {tupla_dados[0][0]}  {tupla_dados[0][1]}%'
          f'\nUnix                   {tupla_dados[1][0]}  {tupla_dados[1][1]}%'
          f'\nLinux                  {tupla_dados[2][0]}  {tupla_dados[2][1]}%'
          f'\nNetware                {tupla_dados[3][0]}  {tupla_dados[3][1]}%'
          f'\nMac os                 {tupla_dados[4][0]}  {tupla_dados[4][1]}%'
          f'\nOutro                  {tupla_dados[5][0]}  {tupla_dados[5][1]}%'
          f'\n------------------------------------'
          f'\nTotal                  {tupla_dados[0][2]} votos')

arg = True
lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []
lista_5 = []
lista_6 = []
while arg:
    opcao = input('Qual o melhor sistema operacional para uso em servidores?')
    print('As possíveis respostas são:\n1-Windows Server\n2-Unix\n3-Linux\n4-Netware\n5-Mac Os\n6-Outro\n0-Sair')
    lista_votos = ['0', '1', '2', '3', '4', '5', '6']
    if opcao in lista_votos:
        if opcao == '1':
            lista_1.append(opcao)
            result1 = len(lista_1)
            print('\nVoto computado, Obrigado!!!\n')
        elif opcao == '2':
            lista_2.append(opcao)
            result2 = len(lista_2)
            print('\nVoto computado, Obrigado!!!\n')
        elif opcao == '3':
            lista_3.append(opcao)
            result3 = len(lista_3)
            print('\nVoto computado, Obrigado!!!\n')
        elif opcao == '4':
            lista_4.append(opcao)
            result4 = len(lista_4)
            print('\nVoto computado, Obrigado!!!\n')
        elif opcao == '5':
            lista_5.append(opcao)
            result5 = len(lista_5)
            print('\nVoto computado, Obrigado!!!\n')
        elif opcao == '6':
            lista_6.append(opcao)
            result6 = len(lista_6)
            print('\nVoto computado, Obrigado!!!\n')
        else:
            votos = (len(lista_1), len(lista_2), len(lista_3), len(lista_4), len(lista_5), len(lista_6))
            resultado_parcial = apurar_votos(votos)
            mostrar_resultado(resultado_parcial)
            arg = False
    else:
        print('\nOption not available, try again!!!\n')
