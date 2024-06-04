# a - print de boas-vindas personalizado
print ('Bem-vindo(a) a Letícia Gonçalves Açaí e Cupuaçu!')
print ('------------------Cardápio------------------')
print ('-' * 44)
print ('---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---')
print ('---|    P    |    R$9.00    |   R$11.00 |---')
print ('---|    M    |   R$14.00    |   R$16.00 |---')
print ('---|    G    |   R$18.00    |   R$20.00 |---')
print ('-' * 44)
print (' ')

lista_de_pedidos = []
cont_erro_sabor = 0
cont_erro_tamanho = 0
# e - acumulador do valor do pedido
valor_total = 0

# g - while, break e continue...
# Primeiro looping que fará o programa ficar rodando
while True:
    #segundo looping que irá verificar a resposta do usuário até que a resposta seja a correta em relação ao sabor
    while True:
        # b - input de sabor
        sabor = (input('Qual sabor você deseja?(AC/CP) ')).upper().strip()
        print (' ')
        # d 1 - if e else validadores de sabor
        if sabor == 'CP' or sabor == 'AC':
            break
        else:
            cont_erro_sabor += 1
            print ('Sabor inválido. Tente novamente [AC/CP]')

    # terceiro looping que verifica a resposta correta em relação ao tamanho
    while True:
        # c - input de tamanho
        tamanho = input(f'Qual o tamanho do seu {sabor}?\nTemos as opções P, M e G\nDigite aqui: ').upper().strip()
        # d 1.2 - if e else validadores de tamanho
        if tamanho =='P' or tamanho == 'M' or tamanho == 'G':
            break
        else:
            cont_erro_tamanho += 1
            print ('Tamanho inválido. Tente novamente [P/M/G]')

    #Verificando preços por tamanhos e sabores
    if tamanho == 'P' and sabor == 'CP':
        valor_total += 9
        lista_de_pedidos.append('Pedido: Cupuaçu Tamanho: P Preço: R$9.00')
        print ('Você pediu um Cupuaçu no tamanho P: R$9.00')
    elif tamanho == 'M' and sabor =='CP':
        valor_total += 14
        print ('Você pediu um Cupuaçu no tamanho M: R$14.00')
        lista_de_pedidos.append('Pedido: Cupuaçu Tamanho: M Preço: R$14.00')
    elif tamanho == 'G' and sabor == 'CP':
        valor_total += 18
        print ('Você pediu um Cupuaçu no tamanho G: R$18.00')
        lista_de_pedidos.append('Pedido: Cupuaçu Tamanho: G Preço: R$18.00')
    elif tamanho == 'P' and sabor == 'AC':
        valor_total += 11
        print ('Você pediu um Açaí no tamanho P: R$11.00')
        lista_de_pedidos.append('Pedido: Açaí    Tamanho: P Preço: R$11.00')
    elif tamanho == 'M' and sabor == 'AC':
        valor_total += 16
        print ('Você pediu um Açaí no tamanho M: R$16.00')
        lista_de_pedidos.append('Pedido: Açaí    Tamanho: M Preço: R$16.00')
    elif tamanho == 'G' and sabor == 'AC':
        valor_total += 20
        print ('Você pediu um Açaí no tamanho G: R$20.00')
        lista_de_pedidos.append('Pedido: Açaí    Tamanho: G Preço: R$20.00')

    #quarto looping que valida se o usuário deseja continuar
    while True:
        # f 1- input validador de continuação do programa
        print (' ')
        continuar = input('Deseja continuar as compras? [S/N]').upper().strip()[0]
        if continuar == 'S' or continuar == 'N':

            break
        else:
            print ('Comando inválido. Tente novamente [S / N]')
            print (' ')
    
    if continuar == 'S':
        continue
    elif continuar == 'N':
        #i = mensagem de boas-vindas personalizada
        print ('-' * 44)
        print ('Obrigada por comprar na Letícia Gonçalves Açaí e Cupuaçu!')
        print ('-' * 44)
        print (' ')
        # j - print de acumulador erro de sabor
        print (f'Você errou {cont_erro_sabor} vezes o pedido dos sabores.')
        # k - print de acumulador de erro de tamanho
        print (f'Você errou {cont_erro_tamanho} vezes o pedido dos tamanhos.')
        print ('-' * 44)

        # l - lista com os pedidos feitos pelo cliente
        for item in lista_de_pedidos:
            print(item)
        print ('-' * 44)

        # f 1.2 - print do acumulador do valor do pedido
        print (f'Valor total da sua compra: R${valor_total:.2f}')
        print ('-' * 44)
        break
print ('Encerrando...')
