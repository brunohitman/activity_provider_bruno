# Alteração na importação da interface
from interfaces.command_interface import Command
from flask import jsonify
import json

class GetCommand(Command):
    def execute(self):
        try:
            # Lógica de processamento para requisições GET
            with open('dados_analytics.json') as json_file:
                data = json.load(json_file)
                result = {'status': 'success', 'message': 'Requisição GET bem-sucedida!', 'data': data}
            
            # Retorna a resposta como JSON
            return jsonify(result), 200
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro
            error_message = str(e)
            result = {'status': 'error', 'message': 'Erro ao processar a requisição', 'error': error_message}
            return jsonify(result), 500
