# Dicionário para armazenar os livros
livros = {}

# Laço para cadastro de livros
while True:
    print("Para cadastrar um livro, insira as informações solicitadas.")
    isbn = input("ISBN do livro: ")
    autor = input("Autor do livro: ")
    titulo = input("Título do livro: ")
    
    # Armazenando o livro no dicionário
    livros[isbn] = f"{autor} - {titulo}"
    
    continuar = input("Deseja cadastrar outro livro? (sim/não): ")
    if continuar != 'sim':
        break

# Laço para pesquisa de livros
while True:
    print("Você pode pesquisar livros por título ou autor.")
    pesquisa = input("Digite o título ou autor do livro: ")
    resultados = []

    # Procurando livros
    for chave in livros:
        if pesquisa in livros[chave]:
            resultados.append(livros[chave])
    
    if len(resultados) > 0:
        print("Livros encontrados:")
        for livro in resultados:
            print(livro)
    else:
        print("Nenhum livro encontrado com essa pesquisa.")
    
    continuar = input("Deseja fazer outra pesquisa? (sim/não): ")
    if continuar != 'sim':
        break