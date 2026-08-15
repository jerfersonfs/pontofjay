from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


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
        "status": "NOVO",
    }


def extrair_precos_oferta(card):
    preco_atual = None
    preco_anterior = None
    desconto = None

    preco_anterior_elemento = card.select_one(".andes-money-amount--previous")

    preco_atual_elemento = card.select_one(".poly-price__amount")

    desconto_elemento = card.select_one(".poly-price__discount-polylabel")

    def converter_preco(elemento):
        if not elemento:
            return None

        fracao = elemento.select_one(".andes-money-amount__fraction")

        if not fracao:
            return None

        valor = fracao.get_text(strip=True)

        # Mercado Livre usa ponto como separador de milhar
        # e, quando houver centavos, eles estarão em outro elemento.
        centavos = elemento.select_one(".andes-money-amount__cents")

        if centavos:
            valor += "." + centavos.get_text(strip=True)

        valor = valor.replace(".", "", valor.count(".") - 1)

        return float(valor.replace(",", "."))

    preco_anterior = converter_preco(preco_anterior_elemento)
    preco_atual = converter_preco(preco_atual_elemento)

    if desconto_elemento:
        texto = desconto_elemento.get_text(strip=True)

        numeros = "".join(caractere for caractere in texto if caractere.isdigit())

        if numeros:
            desconto = int(numeros)

    return preco_atual, preco_anterior, desconto


def extrair_produtos_ofertas(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select(".poly-card")

    produtos = []

    for card in cards:
        titulo = card.select_one(".poly-component__title")
        imagem = card.select_one(".poly-component__picture")
        preco = card.select_one(".poly-component__price")
        link = card.select_one(".poly-component__title")

        url = link.get("href") if link else None

        catalog_id = None
        item_id = None

        if url:
            partes = urlparse(url)

            if "/p/" in partes.path:
                catalog_id = partes.path.split("/p/")[-1]

            parametros = parse_qs(partes.fragment)
            item_id = parametros.get("wid", [None])[0]

        produto = {
            "titulo": titulo.get_text(strip=True) if titulo else None,
            "imagem": imagem.get("src") if imagem else None,
            "preco_html": preco.get_text(" ", strip=True) if preco else None,
            "url": url,
            "catalog_id": catalog_id,
            "item_id": item_id,
        }

        produtos.append(produto)

    return produtos
