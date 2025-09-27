from app.config import Configuracao
from app.repositories.meio_pagamento_repositorio import MeioPagamentoRepositorio
from app.services.meio_pagamento_servicos import MeioPagamentoServico
from app.preprocessors.meio_pagamento_preprocessador import MeioPagamentoProcessador
from app.utils.seguranca import uri_valida

def main():
    # Validação da URI do banco
    if not uri_valida(Configuracao.MONGO_URI):
        raise ValueError("MONGO_URI inválida!")

    repositorio = MeioPagamentoRepositorio(Configuracao.MONGO_URI, Configuracao.MONGO_DB)
    pre_processador = MeioPagamentoProcessador()
    servico = MeioPagamentoServico(Configuracao.BCB_API_URL, pre_processador)
    meios_pagamentos = servico.obter_e_preprocessar()
    for registro in meios_pagamentos:
        repositorio.inserir(registro)
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    main()