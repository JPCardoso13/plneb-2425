from flask import Flask, request, render_template
import json
import re

app = Flask(__name__)

with open("conceitos.json", encoding="utf-8") as json_file:
    DB = json.load(json_file)

### HOME ###
@app.route('/')
def hello_world():
    return render_template("home.html")

### API ###
@app.route('/api/conceitos')
def conceitos_api():
    return DB

@app.post('/api/conceitos')
def adicionar_conceito_api():
    data = request.get_json()
    DB[data["designacao"]] = data["descricao"]
    f_out = open("conceitos.json", "w", encoding="utf-8")
    json.dump(DB, f_out, ensure_ascii=False, indent=4)
    f_out.close()
    return data

@app.route('/api/conceito/<designacao>')
def conceito_api(designacao):
    return {"designacao": designacao, "descricao": DB[designacao]}

### HTML ###
@app.route('/conceitos')
def conceitos():
    designacoes = list(DB.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Designações")

@app.post('/conceitos')
def adicionar_conceito():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")

    DB[designacao] = descricao
    f_out = open("conceitos.json", "w", encoding="utf-8")
    json.dump(DB, f_out, ensure_ascii=False, indent=4)
    f_out.close()

    return render_template("conceitos.html", designacoes=list(DB.keys()), title="Lista de Conceitos")

@app.route('/conceitos/<designacao>')  # TPC5
def conceito(designacao):
    descricao = DB.get(designacao, "Designação não encontrada.")
    return render_template("conceito.html", designacao=designacao, descricao=descricao, title=f"Conceito - {designacao}")

@app.route('/pesquisar')  # TPC6
def pesquisar():
    pesquisa = request.args.get('pesquisa', '')
    palavra_exata = (request.args.get('palavra_exata') == "sim")

    if not pesquisa:
        return render_template("pesquisar.html", resultados=[], avisar_vazio=False)

    pesquisa = rf"\b({re.escape(pesquisa)})\b" if palavra_exata else rf"({re.escape(pesquisa)})"

    resultados = []
    for designacao, descricao in DB.items():
        if (re.search(pesquisa, designacao) is not None) or (re.search(pesquisa, descricao) is not None):
            designacao_bold = re.sub(pesquisa, rf"<strong>\1</strong>", designacao)
            descricao_bold = re.sub(pesquisa, rf"<strong>\1</strong>", descricao)

            resultados.append({
                "designacao": designacao_bold,
                "descricao": descricao_bold,
                "link": f"conceitos/{designacao}"
            })

    return render_template("pesquisar.html", resultados=resultados, avisar_vazio=not bool(resultados))


if __name__ == '__main__':
    app.run(host="localhost", port=6060, debug=True)
