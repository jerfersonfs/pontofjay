from src.ml_api import buscar_produtos
from src.db import criar_tabela, salvar_produto
from src.produtos import extrair_produto
from src.score import calcular_score
from src.score import classificar_score

criar_tabela()

dados = buscar_produtos()

#produtos_api = dados["polycard_client_model"]["polycards"]

#for produto_api in produtos_api:

#    produto = extrair_produto(produto_api)

#    salvar_produto(produto)

#    print(f"Salvo: {produto['titulo']}")
    
produtos_api = dados["polycard_client_model"]["polycards"]

#pprint(produto2)

for produto_api in produtos_api:

    produto = extrair_produto(produto_api)
    score = calcular_score(produto)

    produto["score"] = score
    produto["classificacao"] = classificar_score(score)

    salvar_produto(produto)

    print(f"Salvo: {produto['titulo']}")