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

    return {
        "search": pesquisa,
        "sort": "relevance",
        "filters": [],
        "offset": 0
    }