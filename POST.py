from flask import Flask, request, jsonify
from builder import AnalyticsBuilder

app = Flask(__name__)

# Rota para requisições POST
@app.route('/POST', methods=['POST'])
def post_example():
    try:
        # Recebe os dados do corpo da requisição POST
        data = request.json

        # Use o Builder para construir os dados
        builder = AnalyticsBuilder()
        for analytics_data in data['qualAnalytics']:
            builder.add_data(analytics_data['name'], analytics_data['type'])

        built_data = builder.get_built_data()

        # Faça algo com os dados construídos, como salvá-los em um arquivo
        with open('dados_analytics.json', 'w') as json_file:
            json.dump(built_data, json_file)

        result = {'status': 'success', 'message': 'Dados recebidos e salvos com sucesso!', 'data': built_data}

        # Retorna a resposta como JSON
        return jsonify(result), 200
    except Exception as e:
        # Em caso de erro, retorna uma resposta de erro
        error_message = str(e)
        result = {'status': 'error', 'message': 'Erro ao processar a requisição', 'error': error_message}
        return jsonify(result), 500

if __name__ == '__main__':
    # O host '0.0.0.0' significa que o servidor estará acessível externamente
    app.run(host='0.0.0.0', port=8080)
