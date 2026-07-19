def extrair_produto(produto_api):

    metadata = produto_api["metadata"]

    id_produto = metadata["id"]
    url_produto = metadata["url"]

    product_id = metadata.get("product_id")
    user_product_id = metadata.get("user_product_id")

    tipo_produto = metadata.get("type")
    extra_commission = metadata.get("extra_commission")

    titulo = None
    preco = None
    preco_anterior = None
    desconto = None

    comissao = None

    avaliacao = None
    qtd_vendidos = None

    imagem_id = None

    if produto_api["pictures"]["pictures"]:
        imagem_id = produto_api["pictures"]["pictures"][0]["id"]

    for componente in produto_api["components"]:

        if componente["type"] == "title":

            titulo = componente["title"]["text"]

        elif componente["type"] == "price":

            preco = componente["price"]["current_price"]["value"]

            if "previous_price" in componente["price"]:
                preco_anterior = componente["price"]["previous_price"]["value"]

            if "discount" in componente["price"]:
                desconto = componente["price"]["discount"]["value"]

        elif componente["type"] == "chip":

            texto = componente["chip"]["label"]["text"]

            if "%" in texto:

                numeros = "".join(c for c in texto if c.isdigit())

                if numeros:
                    comissao = f"{numeros}%"

        elif componente["type"] == "review_compacted":

            valores = componente["review_compacted"]["values"]

            for valor in valores:

                if valor.get("key") == "label":
                    avaliacao = valor["label"]["text"]

                elif valor.get("key") == "label2":
                    qtd_vendidos = valor["label"]["text"]

    return {
        "id": id_produto,
        "titulo": titulo,

        "preco": preco,
        "preco_anterior": preco_anterior,
        "desconto": desconto,

        "comissao": comissao,

        "avaliacao": avaliacao,
        "qtd_vendidos": qtd_vendidos,

        "product_id": product_id,
        "user_product_id": user_product_id,

        "tipo_produto": tipo_produto,
        "extra_commission": extra_commission,

        "imagem_id": imagem_id,

        "url_original": url_produto,

        "status": "NOVO"
        
    }