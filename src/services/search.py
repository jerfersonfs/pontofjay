from database.db import adicionar_a_fila

# Main function for interact with user
def obter_payload_busca():

    print("\n========================")
    print("TIPO DE BUSCA")
    print("========================")
    print("1 - Buscar recomendações")
    print("2 - Buscar produto específico")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        return None

    pesquisa = input("\nDigite o produto que deseja pesquisar: ").strip()
    filtros = obter_filtros()
    
    return {
        "search": pesquisa,
        "sort": "relevance",
        "filters": filtros,
        "offset": 0
    }

# Function to catch filters for searchers    
def obter_filtros():
    filtros = []

    print("\n=== FILTROS ===")

    resposta = input("Deseja apenas produtos com comissão extra? (s/n): ")

    if resposta.lower() == "s":
        filtros.append({
            "id": "extra_commission",
            "value": True
        })

    resposta = input("Deseja apenas produtos mais vendidos? (s/n): ")

    if resposta.lower() == "s":
        filtros.append({
            "id": "best_seller",
            "value": True
        })

    return filtros


# Function to save records in database
def selecionar_produtos(produtos):

    print("\n=== PRODUTOS ENCONTRADOS ===")

    for i, produto in enumerate(produtos, start=1):

        print(f"\n[{i}] {produto['titulo']}")
        print(f"    Preço: R$ {produto['preco']}")
        print(f"    Comissão: {produto['comissao']}")

    entrada = input("\nDigite os números dos produtos que deseja gravar (ex: 1,3,7): ")
    indices = []

    for valor in entrada.split(","):
        valor = valor.strip()

        if valor.isdigit():
            indices.append(int(valor) - 1)

    selecionados = []

    for indice in indices:

        if 0 <= indice < len(produtos):
            selecionados.append(produtos[indice])

    return selecionados

# Function to add products in the queue
def destinar_produtos(produtos_selecionados):

    filas_disponiveis = {
        "1": "instagram",
        "2": "tiktok",
        "3": "whatsapp",
        "4": "telegram"
    }

    print("\n=== DESTINO DOS PRODUTOS ===")
    print("1 - Instagram")
    print("2 - TikTok")
    print("3 - WhatsApp")
    print("4 - Telegram")

    escolha = input(
        "\nDigite os números das filas desejadas (ex: 1,2,4): "
    )

    filas_escolhidas = []

    for numero in escolha.split(","):
        numero = numero.strip()

        if numero in filas_disponiveis:
            filas_escolhidas.append(filas_disponiveis[numero])

    if not filas_escolhidas:
        print("Nenhuma fila válida foi selecionada.")
        return

    for produto in produtos_selecionados:

        for fila in filas_escolhidas:

            adicionar_a_fila(
                produto["id"],
                fila
            )

    print("\nProdutos destinados com sucesso!")

def obter_payload_ofertas():
    print("\n========================")
    print("TIPO DE OFERTA")
    print("========================")

    print("1 - Todas as ofertas")
    print("2 - Ofertas relâmpago")

    opcao = input("\nEscolha: ")

    if opcao == "2":
        return {
            "container_id": "MLB779362-1",
            "promotion_type": "lightning"
        }

    return {}