import requests
from config import (AFILIADO_TAG,CSRF_TOKEN,COOKIE)


def gerar_link_afiliado(url_produto):

    url = "https://www.mercadolivre.com.br/affiliate-program/api/v2/stripe/user/links"

    payload = {
        "tag": AFILIADO_TAG,
        "url": url_produto
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://produto.mercadolivre.com.br",
        "Referer": url_produto,
        "User-Agent": "Mozilla/5.0",
        "X-Csrf-Token": CSRF_TOKEN,
        "Cookie": COOKIE
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print("Status:", response.status_code)
    dados = response.json()

    return {
        "link_curto": dados["short_url"],
        "link_longo": dados["long_url"]
    }