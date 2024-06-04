# Lista que irá armazenar os livros cadastrados
lista_livro = []

# Variável global para o ID do livro
id_global = 0

nome = ''
autor = ''
editora = ''

# Função que exibe o menu principal e permite ao usuário escolher uma opção do menu da biblioteca
def menu_principal(lista):
    print('------------ MENU PRINCIPAL ------------')
    escolha = int(input('\n [1] - Cadastrar Livro\n [2] - Consultar Livros\n [3] - Remover livro\n [4] - Sair\nDigite aqui: '))
    if escolha == 1:
        menu_de_cadastar(lista)
    elif escolha == 2:
        menu_de_consulta(lista)
    elif escolha == 3:
        remover_id = int(input('Qual o id do livro que deseja remover do estoque? '))
        remover_por_id(remover_id, lista)
    elif escolha == 4:
        print('Até Logo...')

# Função para o menu de cadastro de livros
def menu_de_cadastar(lista_livro):
    while True:
        print('------------ MENU DE CADASTRAR ------------')
        # Solicita informações sobre o livro ao usuário
        nome = str(input('Digite o Título do livro: '))
        id_global = int(input('Digite o ID: '))
        autor = str(input('Digite o nome do autor: '))
        editora = str(input('Digite o nome da editora: '))

        # Cria um dicionário com as informações do livro e o adiciona à lista de livros
        livro = {
            'id': id_global,
            'nome': nome,
            'autor': autor,
            'editora': editora
        }
        lista_livro.append(livro)
        print('-' *22)
        
        # Verifica se o usuário deseja cadastrar mais livros
        dej = str(input('Deseja cadastrar mais [S/N] ')).upper().strip()[0]
        if dej == 'S':
            continue
        elif dej == 'N':
            break

# Função para o menu de consulta de livros
def menu_de_consulta(lista):
    print('------------ MENU DE CONSULTA ------------')
    opcao = int(input(' [1] - Todos os Livros\n [2] - Consultar Livros por ID\n [3] - Consultar livro por Autor \nDigite aqui: '))
    if opcao == 1:
        encontre__todos_livros(lista)
    elif opcao == 2:
        encontre_por_id(lista)
    elif opcao == 3:
        encontre_por_autor(lista)

# Função para encontrar um livro por ID
def encontre_por_id(lista):
    id = int(input('Qual o ID do livro que deseja encontrar? '))
    for livro in lista:
        if livro['id'] == id:
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            return
    print("Erro: ESSE ID NÃO EXISTE!")

# Função para remover um livro por ID
def remover_por_id(id, lista):
    id = int(input('Qual o ID do livro que deseja remover? '))
    for livro in lista:
        if livro['id'] == id:
            lista.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Erro: ESSE ID NÃO EXISTE!")

# Função para mostrar todos os livros cadastrados
def encontre__todos_livros(lista):
    for item in lista:
        print(item)

# Função para encontrar livros por autor
def encontre_por_autor(lista):
    autor = str(input('Qual autor deseja encontrar? '))
    encontrados = [livro for livro in lista if livro['autor'].lower() == autor.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
    else:
        print("Autor Não Encontrado")

# Mensagem de boas-vindas personalizada
print ('-' * 44)
print('Sejam bem-vindos a Biblioteca da Letícia Gonçalves')
print ('-' * 44)

# Loop principal do programa
while True:
    # Chama o menu principal
    menu_principal(lista_livro)

    # Pergunta ao usuário se deseja voltar ao menu principal
    dej = str(input('Deseja Voltar ao Menu? [S/N] ')).upper().strip()[0]
    if dej == 'S':
        continue
    elif dej == 'N':
        break
