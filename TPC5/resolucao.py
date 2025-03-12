from flask import Flask, request, render_template
import json

app = Flask(__name__)

with open("conceitos.json", encoding="utf-8") as json_file:
    DB = json.load(json_file)

### HOME ###
@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

### API ###
@app.route('/api/conceitos')
def conceitos_api():
    return DB

@app.post('/api/conceitos')
def adicionar_conceito():
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

@app.route('/conceitos/<designacao>')  # TPC5
def conceito(designacao):
    descricao = DB.get(designacao, "Designação não encontrada.")
    return render_template("conceito.html", designacao=designacao, descricao=descricao, title=f"Conceito - {designacao}")

app.run(host="localhost", port=6060, debug=True)
