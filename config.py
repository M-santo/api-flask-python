import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:5000/data")  # URL da API
DB_PATH = os.getenv("DB_PATH", "database.db")  # Caminho do banco de dados
