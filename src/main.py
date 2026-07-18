from api.ml_api import buscar_produtos
from services.extrator import extrair_produto
from services.score import calcular_score, classificar_score
from api.afiliado import gerar_link_afiliado
from database.db import criar_tabela, salvar_produto

#criar_tabela()

dados = buscar_produtos()

produtos_api = dados["polycard_client_model"]["polycards"]

for produto_api in produtos_api:

    produto = extrair_produto(produto_api)
    score = calcular_score(produto)

    produto["score"] = score
    produto["classificacao"] = classificar_score(score)

    link = gerar_link_afiliado(produto["url_original"])

    produto["link_afiliado"] = link["link_curto"]
    produto["link_afiliado_longo"] = link["link_longo"]

    salvar_produto(produto)
    print(f"Salvo: {produto['titulo']}")