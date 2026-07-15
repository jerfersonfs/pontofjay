def extrair_produto(produto_api):

    id_produto = produto_api["metadata"]["id"]
    url_produto = produto_api["metadata"]["url"]

    titulo = None
    preco = None
    comissao = None

    for componente in produto_api["components"]:

        if componente["type"] == "title":
            titulo = componente["title"]["text"]

        elif componente["type"] == "price":
            preco = componente["price"]["current_price"]["value"]

        elif componente["type"] == "chip":
            comissao = componente["chip"]["label"]["text"]

    return {
        "id": id_produto,
        "titulo": titulo,
        "preco": preco,
        "comissao": comissao,
        "url_original": url_produto,
        "status": "NOVO"
    }
