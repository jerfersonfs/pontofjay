from src.ml_api import buscar_produtos
from src.db import criar_tabela, salvar_produto
from src.produtos import extrair_produto

criar_tabela()

dados = buscar_produtos()

produtos_api = dados["polycard_client_model"]["polycards"]

for produto_api in produtos_api:

    produto = extrair_produto(produto_api)

    salvar_produto(produto)

    print(f"Salvo: {produto['titulo']}")