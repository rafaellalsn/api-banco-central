import requests
from app.models.meio_pagamento import MeioPagamento

# Service para lidar com coleta da API e pré-processamento
class MeioPagamentoServico:

    def __init__(self, url_api, pre_processador):
        self.url_api = url_api
        self.pre_processador = pre_processador

    def obter_e_preprocessar(self):
        resposta = requests.get(self.url_api)
        resposta.raise_for_status()
        dados = resposta.json()
        dados_brutos = dados.get("value", [])
        # Pré-processa cada item da resposta
        processados = [self.pre_processador.processar(item) for item in dados_brutos]
        return processados
    