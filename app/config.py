import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

class Configuracao:
    MONGO_URI = os.getenv('MONGO_URI')
    BCB_API_URL = os.getenv('BCB_API_URL')
    MONGO_DB = os.getenv('MONGO_DB')