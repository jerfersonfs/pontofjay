import requests


def montar_url_imagem(imagem_id, template):

    return (
        template.replace("{square}", "Q")
        .replace("{2x}", "")
        .replace("{id}", imagem_id)
        .replace("{size}", "AB")
        .replace("{sanitized_title}", "")
    )


def baixar_imagem(url, imagem_id):
    try:

        resposta = requests.get(url)

        resposta.raise_for_status()

        caminho = f"downloads/imagens/{imagem_id}.webp"

        with open(caminho, "wb") as arquivo:
            arquivo.write(resposta.content)

        return caminho

    except requests.exceptions.RequestException as erro:

        print(f"Erro ao baixar imagem {imagem_id}: {erro}")
        return None
