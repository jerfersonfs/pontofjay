import requests


def buscar_produtos():
    url = "https://www.mercadolivre.com.br/affiliate-program/api/hub/search?is_affiliate=true&device=desktop"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.mercadolivre.com.br",
        "Referer": "https://www.mercadolivre.com.br/afiliados/hub?is_affiliate=true",
        "User-Agent": "Mozilla/5.0",
        "X-Csrf-Token": "VdF6w9Pq-JfhFfx5V0wbsM7EHOza60eom3jk"
    }
    payload = {
        "search": "",
        "sort": "relevance",
        "filters": [
            {
                "id": "extra_commission",
                "value": True
            }
        ],
        "offset": 0
    }
    cookies = {
    "orguserid": "dTThTh0dddhh",
    "orgnickp": "FRJE328144",
    "ssid": "ghy-070818-xYUzRyQY2Rg38dtVDcoUWc83z9QqNf-__-444100077-__-1878244212617--RRR_0-RRR_0",
    }

    response = requests.post(
        url=url,
        headers=headers,
        cookies=cookies,
        json=payload
    )

    print(f"Status: {response.status_code}")

    return response.json()