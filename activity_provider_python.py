from flask import Flask, render_template, jsonify, send_from_directory
from GET import get_example  # Importa a função get_example do GET.py
from POST import post_example  # Importa a função post_example do POST.py

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para trazer o JSON de config_param.json
@app.route('/json-params-atividade')
def json_params_atividade():
    try:
        return send_from_directory('params', 'config_param.json', as_attachment=True)
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro ao obter o JSON', 'error': str(e)}), 500

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
