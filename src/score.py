def calcular_score(produto):

    score = 0

    # Comissão
    comissao = int(produto["comissao"].replace("%", ""))

    if comissao >= 30:
        score += 5
    elif comissao >= 25:
        score += 4
    elif comissao >= 20:
        score += 3
    elif comissao >= 15:
        score += 2
    else:
        score += 1

    # Avaliação
    avaliacao = float(produto["avaliacao"])

    if avaliacao >= 4.8:
        score += 3
    elif avaliacao >= 4.5:
        score += 2
    elif avaliacao >= 4.0:
        score += 1

    # Desconto
    desconto = produto["desconto"] or 0

    if desconto >= 40:
        score += 3
    elif desconto >= 25:
        score += 2
    elif desconto >= 10:
        score += 1

    # Extra commission
    if produto["extra_commission"] == "true":
        score += 5

    return score


def classificar_score(score):

    if score >= 16:
        return "Excelente"

    elif score >= 12:
        return "Muito bom"

    elif score >= 8:
        return "Bom"

    elif score >= 5:
        return "Regular"

    return "Fraco"