import json
from bs4 import BeautifulSoup
import requests


BASE_URL = "https://www.atlasdasaude.pt"


def get_html_content(url):
    response = requests.get(url)
    html_content = response.text
    print(f"Obtido o conteúdo html de {response.url}")

    return html_content


def get_info_doencas(letra):
    url = f"{BASE_URL}/doencasaaz/{letra}"
    html_content = get_html_content(url)

    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}
    for div_row in soup.find_all('div', class_="views-row"):
        designacao = div_row.div.h3.a.text

        resumo_div = div_row.find('div', class_="views-field-body")
        resumo = resumo_div.div.text.strip().replace(" ", " ")

        url_doenca = div_row.div.h3.a['href']

        doencas[designacao] = {
            "URL": url_doenca,
            "Resumo": resumo,
            "Conteúdo": get_conteudo_doenca(url_doenca),
        }

    return doencas


def get_conteudo_doenca(url_doenca):
    html_content = get_html_content(f"{BASE_URL}{url_doenca}")

    soup = BeautifulSoup(html_content, 'html.parser')
    div_content = soup.find('div', class_="node-doencas")

    return format_contents_as_dict(div_content)


def format_contents_as_dict(html_content):
    content_map = {"Data": html_content.find("div", class_="field-name-post-date").text.strip()}

    current_key = "Descrição"
    content_map[current_key] = []

    artigos_relacionados = {}  # Hard-coded para ficar com uma formatação melhor

    for element in html_content.find("div", class_="field-name-body").div.div:
        if element.name == "h2":
            current_key = element.text.strip().replace(" ", " ")
            content_map[current_key] = []

        elif element.name == "p" or element.name == "div":
            content_map[current_key].append(element.text.strip().replace(" ", " "))

        elif element.name == "ul":
            content_map[current_key].append([li.text.strip().replace(" ", " ") for li in element.find_all("li")])

        elif element.name == "h3":
            artigos_relacionados |= {element.text.strip().replace(" ", " "): element.a["href"]}
            content_map[current_key] = artigos_relacionados

    return content_map | get_last_elems(html_content)


def get_last_elems(html_content):
    raw_outside_elems = [
        html_content.find("div", class_="field-name-field-fonte"),
        html_content.find("div", class_="field-name-field-site"),
        html_content.find("div", class_="field-name-field-nota")
    ]

    outside_elems = {}
    for elem in raw_outside_elems:
        if elem:
            key = elem.find("div", class_="field-label").text.strip().replace(" ", " ").replace(":", "")
            value = elem.find("div", class_="field-items").text.strip().replace(" ", " ").replace(":", "")
            outside_elems[key] = value

    return outside_elems


if __name__ == "__main__":
    res = {}
    for ascii_code in range(ord('a'), ord('z') + 1):
        letra = chr(ascii_code)
        res |= get_info_doencas(letra)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
