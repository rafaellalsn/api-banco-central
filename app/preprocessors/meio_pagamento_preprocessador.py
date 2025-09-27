from app.models.meio_pagamento import MeioPagamento

# Realiza etapas de limpeza/validação/conversão
class MeioPagamentoProcessador:
    def processar(self, data):
        # Valida e converte os campos conforme necessário
        data_str = data.get("AnoMes")
        quantidade_pix = int(data.get("quantidadePix", 0))
        valor_pix = float(data.get("valorPix", 0))
        quantidade_ted = int(data.get("quantidadeTED", 0))
        valor_ted = float(data.get("valorTED", 0))
        quantidade_tec = int(data.get("quantidadeTEC", 0))
        
        return MeioPagamento(
            data_str, quantidade_pix, valor_pix,
            quantidade_ted, valor_ted, quantidade_tec
        )
    


    