from flask import Flask, render_template, jsonify, send_from_directory
import json
from GET import get_example as get_request
from POST import post_example as post_request
from postgres_fetcher import PostgreSQLFetcher
import psycopg2

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para trazer o JSON de config_param.json
@app.route('/parametros_atividade')
def json_params_atividade():
    try:
        with open('params/config_param.json') as json_file:
            data = json.load(json_file)
            return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro ao obter o JSON', 'error': str(e)}), 500

# Rota para trazer o JSON de analytics_url.json
@app.route('/parametros_analiticas')
def list_analytics():
    try:
        with open('params/analytics_url.json') as json_file:
            data = json.load(json_file)
            return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro ao obter o analytics_url.json', 'error': str(e)}), 500

# Rota para trazer o JSON de analytics_list_url.json
@app.route('/analiticas')
def analytics():
    try:
        with open('analytics/analytics_list_url.json') as json_file:
            data = json.load(json_file)
            return jsonify(data)
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Erro ao obter o analytics_list_url.json', 'error': str(e)}), 500

# Rota específica para lidar com requisições GET
@app.route('/GET', methods=['GET'])
def get_saved_data():
    return get_request()

# Rota específica para lidar com requisições POST
@app.route('/POST', methods=['POST'])
def handle_post_request():
    return post_request()

# Rota para configurar a atividade
@app.route('/config_url.html')
def config_url():
    return render_template('config_url.html')

@app.route('/consultar_analiticas', methods=['GET'])
def consultar_analiticas():
    try:
        fetcher = PostgreSQLFetcher()
        data = fetcher.fetch_data()

        if data:
            return render_template('resultado_analiticas.html', data=data)
        else:
            return jsonify({'status': 'error', 'message': 'Nenhum dado encontrado'}), 404

    except Exception as e:
        error_message = str(e)
        return jsonify({'status': 'error', 'message': 'Erro ao consultar as analíticas', 'error': error_message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
