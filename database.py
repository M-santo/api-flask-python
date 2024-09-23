import sqlite3

def get_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            value REAL)
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")
