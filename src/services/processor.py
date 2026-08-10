from api.ml_api import buscar_produtos
from api.afiliado import gerar_link_afiliado
from database.db import (criar_tabela, salvar_produto)
from services.extrator import extrair_produto
from services.score import calcular_score, classificar_score
from services.images import baixar_imagem, montar_url_imagem
from services.search import obter_payload_busca
from services.search import selecionar_produtos
 
def processar_produto(produto, template):

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

    baixar_imagem(url_imagem, produto["imagem_id"])
    salvar_produto(produto)

def executar_pipeline():

    criar_tabela()

    payload = obter_payload_busca()
    dados = buscar_produtos(payload)
    template = dados["polycard_client_model"]["polycard_context"]["picture_template"]
    produtos_api = dados["polycard_client_model"]["polycards"]
    print(f"{len(produtos_api)} produtos encontrados.")

    produtos = []

    for produto_api in produtos_api:

        try:
            produto = extrair_produto(produto_api)
            produtos.append(produto)
        except Exception as erro:
            print(f"Erro ao extrair produto: {erro}")

    selecionados = selecionar_produtos(produtos)

    print(f"\n{len(selecionados)} produtos selecionados.")


    for produto in selecionados:
        try:
            processar_produto(produto, template)
        except Exception as erro:
            print(f"Erro ao processar produto: {erro}")