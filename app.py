from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data_str = request.json.get("data")
    dias_lista = request.json.get("dias_lista", [])

    if not data_str or not dias_lista:
        return jsonify({"erro": "Informe a data e os dias corretamente."}), 400

    data_emissao = datetime.strptime(data_str, "%Y-%m-%d")

    resultados = []
    for i, dias in enumerate(dias_lista, start=1):
        data_parcela = data_emissao + timedelta(days=int(dias))
        resultados.append({
            "parcela": i,
            "dias": dias,
            "data": data_parcela.strftime("%d/%m/%Y")
        })

    return jsonify(resultados)

if __name__ == "__main__":
    # Usa Waitress (servidor compatível com Render)
    serve(app, host="0.0.0.0", port=5000)
