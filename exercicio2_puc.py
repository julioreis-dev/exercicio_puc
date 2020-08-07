def calcular(lista):
    somatorio = 0
    for n in lista:
        somatorio = somatorio+n
    media = somatorio/len(lista)
    return media


arg = True
while arg:
    lista_resultado = []
    atleta = input('\nAtleta: ')
    salto1 = float(input('Primeiro salto: '))
    lista_resultado.append(salto1)
    salto2 = float(input('Segundo salto: '))
    lista_resultado.append(salto2)
    salto3 = float(input('Terceiro salto: '))
    lista_resultado.append(salto3)
    salto4 = float(input('Quarto salto: '))
    lista_resultado.append(salto4)
    salto5 = float(input('Quinto salto: '))
    lista_resultado.append(salto5)
    media_calculada = calcular(lista_resultado)
    if atleta != '':
        print(f"Atleta: {atleta}"
              f"\nPrimeiro salto: {salto1} m"
              f"\nSegundo salto: {salto2} m"
              f"\nTerceiro salto: {salto3} m"
              f"\nQuarto salto: {salto4} m"
              f"\nQuinto salto: {salto4} m"
              "\n\nResultado Final:"
              f"\nAtleta: {atleta}"
              f"\nSaltos: {salto1} - {salto2} - {salto3} - {salto4} - {salto5}"
              f"\nMédia dos saltos: {media_calculada} m")
    else:
        print('Fim da aplicação')
        arg = False
