import requests

def montar_url_imagem(imagem_id, template):

    return (
        template
        .replace("{square}", "Q")
        .replace("{2x}", "")
        .replace("{id}", imagem_id)
        .replace("{size}", "AB")
        .replace("{sanitized_title}", "")
    )

def baixar_imagem(url, imagem_id):
    print("URL:")
    print(repr(url))

    resposta = requests.get(url)

    if resposta.status_code == 200:

        caminho = f"downloads/imagens/{imagem_id}.webp"

        with open(caminho, "wb") as arquivo:
            arquivo.write(resposta.content)

        return caminho

    return None