estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip().capitalize()
    if nome in estoque:
        print("Este produto já existe no estoque.")
        return
    try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[nome] = {"nome": nome, "preco": preco, "quantidade": quantidade}
        print(f"Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para preço e quantidade.")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ").strip().capitalize()
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def listar_produtos():
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print("\n--- Produtos em Estoque ---")
    for nome, dados in estoque.items():
        print(f"Nome: {dados['nome']}")
        print(f"  Preço: R${dados['preco']:.2f}")
        print(f"  Quantidade: {dados['quantidade']}")
        print("-" * 25)

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ").strip().capitalize()
    if nome not in estoque:
        print(f"Produto '{nome}' não encontrado no estoque.")
        return
    
    print(f"\nAtualizando produto: {nome}")
    print("O que você gostaria de atualizar?")
    print("1 - Preço")
    print("2 - Quantidade")
    
    opcao = input("Digite sua opção: ")
    
    try:
        if opcao == "1":
            novo_preco = float(input("Digite o novo preço: "))
            estoque[nome]["preco"] = novo_preco
            print("Preço atualizado com sucesso!")
        elif opcao == "2":
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome]["quantidade"] = nova_quantidade
            print("Quantidade atualizada com sucesso!")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número.")


while True:
    print("\n Menu principal")
    print("1 - Adicionar um novo produto")
    print("2 - Remover um produto")
    print("3 - Listar todos os produtos")
    print("4 - Atualizar informações de um produto")
    print("5 - Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        remover_produto()
    elif opcao == "3":
        listar_produtos()
    elif opcao == "4":
        atualizar_produto()
    elif opcao == "5":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 5.")
