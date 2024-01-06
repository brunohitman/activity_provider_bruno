from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask(__name__)

def create_table_if_not_exists():
    # Conectar ao banco de dados
    conn = psycopg2.connect("postgres://db_activity_provider_user:L8hE1UxGVmADUsMARVKDB4CXoFdKMzu9@dpg-cmcsdq021fec73cub2f0-a.oregon-postgres.render.com/db_activity_provider")
    
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()
    
    # Comando SQL para criar tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Relatorios_Analiticos_Recebidos (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL
    );
    """
    
    # Executar o comando SQL
    cursor.execute(create_table_query)
    
    # Confirmar a execução do comando
    conn.commit()
    
    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()

@app.route('/POST', methods=['POST'])
def post_example():
    try:
        # Verificar e criar tabela se não existir
        create_table_if_not_exists()
        
        # Receber dados do corpo da requisição POST
        data = request.json

        # Conectar ao banco de dados
        conn = psycopg2.connect("postgres://db_activity_provider_user:L8hE1UxGVmADUsMARVKDB4CXoFdKMzu9@dpg-cmcsdq021fec73cub2f0-a.oregon-postgres.render.com/db_activity_provider")
        
        # Criar um cursor para inserir dados
        cursor = conn.cursor()
        
        # Inserir cada registro na tabela
        for analytics_data in data['qualAnalytics']:
            cursor.execute("INSERT INTO Relatorios_Analiticos_Recebidos (name, type) VALUES (%s, %s)", (analytics_data['name'], analytics_data['type']))
        
        # Confirmar a inserção dos dados
        conn.commit()
        
        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()

        result = {'status': 'success', 'message': 'Dados recebidos e salvos com sucesso!'}
        
        # Retorna a resposta como JSON
        return jsonify(result), 200
    
    except Exception as e:
        # Em caso de erro, retorna uma resposta de erro
        error_message = str(e)
        result = {'status': 'error', 'message': 'Erro ao processar a requisição', 'error': error_message}
        return jsonify(result), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)