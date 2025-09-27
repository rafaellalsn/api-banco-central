from pymongo import MongoClient

# Responsável por acessar o banco de dados
class MeioPagamentoRepositorio:
    def __init__(self, mongo_uri, mongo_db):
        self.cliente = MongoClient(mongo_uri)
        self.colecao = self.cliente[mongo_db]["meios_pagamentos"]

    def inserir(self, meio_pagamento):
        # Insere um documento moeda na coleção
        self.colecao.insert_one(meio_pagamento.to_dict())