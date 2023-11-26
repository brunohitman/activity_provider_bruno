from flask import jsonify

# Função para lidar com requisições GET
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
