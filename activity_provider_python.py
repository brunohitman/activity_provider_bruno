from flask import Flask, render_template, jsonify
from GET import get_example  # Importa a função get_example do GET.py
from POST import post_example  # Importa a função post_example do POST.py

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota dinâmica que chama a função do GET.py ou do POST.py
@app.route('/<path:path>', methods=['GET', 'POST'])
def dynamic_route(path):
    if path == 'GET':
        return get_example()
    elif path == 'POST':
        return post_example()
    elif path == 'config_url.html':
        return render_template('config_url.html')
    else:
        return jsonify({'status': 'error', 'message': 'Rota não encontrada'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
