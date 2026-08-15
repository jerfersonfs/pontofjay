import requests


def buscar_produtos(payload=None):
    url = "https://www.mercadolivre.com.br/affiliate-program/api/hub/search?is_affiliate=true&device=desktop"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.mercadolivre.com.br",
        "Referer": "https://www.mercadolivre.com.br/afiliados/hub?is_affiliate=true",
        "User-Agent": "Mozilla/5.0",
        "X-Csrf-Token": "VdF6w9Pq-JfhFfx5V0wbsM7EHOza60eom3jk",
    }
    cookies = {
        "orguserid": "dTThTh0dddhh",
        "orgnickp": "FRJE328144",
        "ssid": "ghy-070818-xYUzRyQY2Rg38dtVDcoUWc83z9QqNf-__-444100077-__-1878244212617--RRR_0-RRR_0",
    }

    try:
        if payload is None:
            payload = {"search": "", "sort": "relevance", "filters": [], "offset": 0}

        response = requests.post(
            url=url, headers=headers, cookies=cookies, json=payload
        )
        print("\nPayload enviado:")
        print(payload)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao buscar produtos: {erro}")
        return None


def buscar_ofertas(params=None):
    url = "https://www.mercadolivre.com.br/ofertas"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    try:
        response = requests.get(url=url, headers=headers, params=params)

        print("\nURL acessada:")
        print(response.url)

        print("Status:", response.status_code)
        print("Tamanho da resposta:", len(response.text))

        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao buscar ofertas: {erro}")
        return None
