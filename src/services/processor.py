from api.ml_api import buscar_produtos
from api.afiliado import gerar_link_afiliado

from database.db import (criar_tabela, salvar_produto, produto_existe)

from services.extrator import extrair_produto
from services.score import calcular_score, classificar_score
from services.images import baixar_imagem, montar_url_imagem
from services.search import obter_payload_busca


def processar_produto(produto_api, template):
    
    produto = extrair_produto(produto_api)

    if produto_existe(produto["id"]):
        print(f"Produto já existe: {produto['titulo']}")
        return

    score = calcular_score(produto)
    produto["score"] = score
    produto["classificacao"] = classificar_score(score)

    link = gerar_link_afiliado(produto["url_original"])
    produto["link_afiliado"] = link["link_curto"]
    produto["link_afiliado_longo"] = link["link_longo"]

    url_imagem = montar_url_imagem(
        produto["imagem_id"],
        template
    )

    caminho_imagem = baixar_imagem(
        url_imagem,
        produto["imagem_id"]
    )

    # Vamos usar isso futuramente
    produto["caminho_imagem"] = caminho_imagem

    salvar_produto(produto)


def executar_pipeline():

    criar_tabela()

    payload = obter_payload_busca()

    dados = buscar_produtos(payload)

    template = dados["polycard_client_model"]["polycard_context"]["picture_template"]

    produtos_api = dados["polycard_client_model"]["polycards"]

    print(f"{len(produtos_api)} produtos encontrados.")

    for produto_api in produtos_api:

        try:
            processar_produto(produto_api, template)

        except Exception as erro:
            print(f"Erro ao processar produto: {erro}")