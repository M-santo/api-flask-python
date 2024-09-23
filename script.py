import requests
import schedule
import time
import logging
from config import API_URL, DB_PATH
from database import get_connection, create_tables

# Configurar o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_api_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição: {e}")
        return None

def process_data(data):
    if not data:
        return []
    
    processed_data = []
    for item in data:
        processed_item = {
            'id': item['id'],
            'name': item['name'].upper(),
            'value': float(item['value']) * 1.1  # Aumento de 10%
        }
        processed_data.append(processed_item)
    return processed_data

def store_data(data, db_path):
    if not data:
        logging.info("Nenhum dado para armazenar.")
        return
    
    conn = get_connection(db_path)
    if conn is None:
        return
    
    create_tables(conn)
    cursor = conn.cursor()
    
    try:
        for item in data:
            cursor.execute('''
            INSERT OR REPLACE INTO items (id, name, value)
            VALUES (?, ?, ?)
            ''', (item['id'], item['name'], item['value']))
        conn.commit()
        logging.info(f"{len(data)} itens armazenados no banco de dados.")
    except sqlite3.Error as e:
        logging.error(f"Erro ao armazenar dados: {e}")
    finally:
        conn.close()

def job():
    logging.info(f"Tentando acessar a API: {API_URL}")
    data = get_api_data(API_URL)
    
    if data:
        processed_data = process_data(data)
        store_data(processed_data, DB_PATH)
        logging.info("Dados atualizados com sucesso.")
    else:
        logging.error("Falha ao recuperar dados da API.")

# Executar imediatamente
job()

# Agendar o job para rodar a cada hora
schedule.every(1).hour.do(job)

# Manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(1)
