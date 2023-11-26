from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para requisições GET
@app.route('https://activity-provider-bruno.onrender.com', methods=['GET'])
def get_example():
    try:
        # Lógica de processamento para requisições GET
        result = {'status': 'success', 'message': 'Requisição GET bem-sucedida!'}
        
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
