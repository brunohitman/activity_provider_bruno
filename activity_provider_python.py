from flask import Flask, jsonify
from GET import get_example  # Importa a função get_example do GET.py

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Rota dinâmica que chama a função do GET.py
@app.route('/<path:path>', methods=['GET'])
def dynamic_route(path):
    if path == 'GET':
        return get_example()
    else:
        return jsonify({'status': 'error', 'message': 'Rota não encontrada'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
