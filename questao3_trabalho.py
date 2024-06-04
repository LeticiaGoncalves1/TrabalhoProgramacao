# Mensagem de boas-vindas
print('Bem-vindo(a) a Letícia Gonçalves Copiadora')

def escolha_servico():
    servicos = {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}
    while True:
        servico = input("Digite o serviço desejado (DIG/ICO/IPB/FOT): ").strip().upper()
        if servico in servicos:
            return servicos[servico]
        else:
            print("Opção inválida. Por favor, escolha entre DIG, ICO, IPB ou FOT.")

def calcular_desconto(num_paginas):
    if num_paginas >= 20000:
        print("Número de páginas excede o limite permitido de 20000.")
        return None
    elif num_paginas >= 2000:
        return num_paginas * 0.75
    elif num_paginas >= 200:
        return num_paginas * 0.80
    elif num_paginas >= 20:
        return num_paginas * 0.85
    else:
        return num_paginas

def num_pagina():
    while True:
        try:
            num_paginas = int(input("Quantas páginas você deseja? "))
            desconto_aplicado = calcular_desconto(num_paginas)
            if desconto_aplicado is not None:
                return desconto_aplicado
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def servico_extra():
    extras = {1: 15.00, 2: 40.00, 0: 0.00}
    while True:
        try:
            extra = int(input("Deseja algum serviço extra? "))
            if extra in extras:
                return extras[extra]
            else:
                print("Opção inválida. Por favor, escolha entre 1, 2 ou 0.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    valor_total = 0  # Variável para armazenar o valor total da compra

    while True:
        #serviços disponíveis
        print('-' * 50)
        print('| Serviços disponíveis:             |   Preços:  |')
        print('| [DIG] - Digitalização             |   R$1,10   |')
        print('| [ICO] - Impressão Colorida        |   R$1,00   |')
        print('| [IPB] - Impressão Preto e Branco  |   R$0,40   |')
        print('| [FOT] - Fotocópia                 |   R$0,20   |')
        print('-' * 50)

        # Escolha do serviço
        valor_servico = escolha_servico()

        # Número de páginas com desconto
        numero_paginas = num_pagina()

        # Serviço extra
        print(' ')
        print('Temos opções de encaderamentos, tem interesse?')
        print('[1] encadernamento simples      - R$15,00')
        print('[2] encadernamento de capa dura - R$40,00')
        print('[0] Não desejo mais nada.')
        valor_extra = servico_extra()

        # Cálculo total do pedido atual
        total_pedido = (valor_servico * numero_paginas) + valor_extra
        print(f"Total do pedido atual: R$ {total_pedido:.2f}")

        # Adiciona o total do pedido atual ao valor final da compra
        valor_total += total_pedido

        # Exibindo o total da compra no momento
        print (' ')
        print(f"Valor da compra até agora: R$ {valor_total:.2f}")

        # Opção de sair ou reiniciar
        continuar =''
        while continuar != 'S' and continuar != 'N':
            continuar = input("Deseja realizar outro pedido? (S/N): ").strip().upper()
            if continuar == 'S':
                break
            elif continuar == 'N':
                print ('-' * 50)
                print(f"Total final a pagar: R$ {valor_total:.2f}")
                print("Obrigado por usar o sistema de cobrança de serviços da Letícia Gonçalves Copiadora!")
                break
        if continuar == 'S':
            continue
        elif continuar == 'N':
            break

# Executando a função principal
if __name__ == "__main__":
    main()
