from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados em memória
estoque = [
    {"id": 1, "nome": "Produto 1", "quantidade": 10},
    {"id": 2, "nome": "Produto 2", "quantidade": 5},
    # Adicione mais itens, se necessário
]

@app.route('/')
def index():
    return render_template('index.html', estoque=estoque)

@app.route('/api/estoque', methods=['GET'])
def get_estoque():
    return jsonify(estoque)

@app.route('/api/estoque', methods=['POST'])
def add_item():
    data = request.get_json()
    novo_item = {
        "id": len(estoque) + 1,
        "nome": data['nome'],
        "quantidade": data['quantidade']
    }
    estoque.append(novo_item)
    return jsonify({"message": "Item adicionado com sucesso!"})

# Outras rotas para atualizar e excluir itens também devem ser adicionadas.

if __name__ == '__index__':
    app.run(debug=True)