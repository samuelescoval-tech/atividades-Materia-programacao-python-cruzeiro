# Projeto 2 - Sistema simples de controle de estoque

# Estrutura de dados inicial do estoque
# O dicionário permite acessar e atualizar os produtos pelo nome
estoque = {
    "Notebook": [10, 3500.00],
    "Mouse": [50, 80.00],
    "Teclado": [30, 150.00]
}

# Laço de repetição principal do sistema
while True:
    print("\n--- MENU DE ESTOQUE ---")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    opcao = input("Escolha uma opção (1 a 4): ")

    # Opção 1 - Visualizar estoque
    if opcao == "1":
        print("\n--- PRODUTOS EM ESTOQUE ---")

        for nome_produto in estoque:
            dados_produto = estoque[nome_produto]
            quantidade_atual = dados_produto[0]
            preco_produto = dados_produto[1]

            print(
                f"Produto: {nome_produto} | "
                f"Quantidade: {quantidade_atual} | "
                f"Preço: R${preco_produto:.2f}"
            )

    # Opção 2 - Registrar entrada de produto
        
    elif opcao == "2":
        print("\n--- ENTRADA DE PRODUTO ---")

        nome_produto = input("Digite o nome do produto: ")

        # Converte o valor digitado de string para inteiro
        quantidade_entrada = int(input("Digite a quantidade que está entrando: "))

        if nome_produto in estoque:
            estoque[nome_produto][0] += quantidade_entrada
            print("Quantidade atualizada com sucesso!")

        else:
            print("Produto não encontrado no estoque.")
            cadastrar = input("Deseja cadastrar este novo produto? (s/n): ").lower()

            if cadastrar == "s":
                # Converte o valor digitado de string para float
                preco_produto = float(input("Digite o preço do produto: "))

                estoque[nome_produto] = [quantidade_entrada, preco_produto]

                print("Produto cadastrado com sucesso!")
            else:
                print("Entrada cancelada.")

    # Opção 3 - Registrar saída de produto
    elif opcao == "3":
        print("\n--- SAÍDA DE PRODUTO ---")

        nome_produto = input("Digite o nome do produto: ")

        if nome_produto not in estoque:
            print("Produto não encontrado.")
        else:
            # Converte o valor digitado de string para inteiro
            quantidade_saida = int(input("Digite a quantidade que está saindo: "))

            quantidade_atual = estoque[nome_produto][0]

            if quantidade_saida > quantidade_atual:
                print("Estoque insuficiente.")
            else:
                estoque[nome_produto][0] -= quantidade_saida
                print("Saída realizada com sucesso!")

    # Opção 4 - Encerrar sistema
    elif opcao == "4":
        print("Encerrando o sistema. Até mais!")
        break

    # Tratamento para opção inválida
    else:
        print("Opção inválida! Tente novamente.")