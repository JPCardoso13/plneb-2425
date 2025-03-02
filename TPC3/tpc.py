import re


file = open(r'..\..\info-pln-2025\data\dicionario_medico.txt', encoding='utf-8')
texto = file.read()


# Limpeza do ficheiro
texto = re.sub(r"\f", "", texto)


# Marcação de designações
texto = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", texto)


# Formatação do conteúdo de uma descrição
def limpar_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r"\n", " ", descricao)
    return descricao


# Extração de conceitos
conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)
conceitos = [(designacao, limpar_descricao(descricao)) for designacao, descricao in conceitos_raw]


# Gerar HTML
def gerar_html(conceitos):
    html_header = """
        <!DOCTYPE html>
            <head>
            <meta charset="UTF-8"/>
            </head>
            <body>
            <h3>Dicionário de Conceitos Médicos</h3>
            <p>Este dicionário foi desenvolvido para a aula 3 de PLNEB-2025.</p>
        """

    html_conceitos = ""

    for designacao, descricao in conceitos:
        html_conceitos += f"""
        <div>
            <p><b>{designacao}</b></p>
            <p>{descricao}</p>
        </div>
        <hr/>    
        """

    html_footer = """
        </body>
    </html>
    """

    return html_header + html_conceitos + html_footer

html_text = gerar_html(conceitos)
html_output = open("output.html", "w", encoding="utf-8")
html_output.write(html_text)
html_output.close()

file.close()
