from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path("cupcakes_larissa.db")

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS pedidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Confirmado'
        )""")

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    init_db()
    dados = request.get_json(force=True)
    campos = ["cliente","telefone","endereco","total"]
    faltando = [c for c in campos if not dados.get(c)]
    if faltando:
        return jsonify({"erro":"Campos obrigatórios ausentes","campos":faltando}),400
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            "INSERT INTO pedidos(cliente,telefone,endereco,total) VALUES(?,?,?,?)",
            (dados["cliente"],dados["telefone"],dados["endereco"],float(dados["total"]))
        )
        pedido_id = cur.lastrowid
    return jsonify({"pedido_id":pedido_id,"status":"Confirmado"}),201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
