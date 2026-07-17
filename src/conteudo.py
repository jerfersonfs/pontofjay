def gerar_conteudo(produto):

    titulo = (
        f"{produto['titulo']} | "
        f"{produto['comissao']} de comissão 🔥"
    )

    legenda = f"""
✅ Avaliação: {produto['avaliacao']}
✅ Vendidos: {produto['qtd_vendidos']}
✅ Desconto: {produto['desconto']}%

Produto com potencial de venda e alta comissão para afiliados.
"""

    cta = "Confira a oferta através do link de afiliado."

    return {
        "titulo": titulo,
        "legenda": legenda.strip(),
        "cta": cta
    }