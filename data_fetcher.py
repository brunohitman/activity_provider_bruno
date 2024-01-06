import psycopg2

def fetch_data_from_db():
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect("postgres://db_activity_provider_user:L8hE1UxGVmADUsMARVKDB4CXoFdKMzu9@dpg-cmcsdq021fec73cub2f0-a.oregon-postgres.render.com/db_activity_provider")
        
        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executar a consulta SQL
        cursor.execute("SELECT name, type FROM Relatorios_Analiticos_Recebidos")
        
        # Buscar todos os registros
        data = cursor.fetchall()

        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()

        return data

    except Exception as e:
        print(f"Erro ao buscar dados do banco de dados: {e}")
        return None
