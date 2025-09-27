

class MeioPagamento:

    def __init__(self, data, quantidade_pix, valor_pix,
                 quantidade_ted, valor_ted, quantidade_tec):
        self.data = data
        self.quantidade_pix = quantidade_pix
        self.valor_pix = valor_pix
        self.quantidade_ted = quantidade_ted
        self.valor_ted = valor_ted
        self.quantidade_tec = quantidade_tec

    def to_dict(self):
        return {
            "data": self.data,
            "quantidade_pix": self.quantidade_pix,
            "valor_pix": self.valor_pix,
            "quantidade_ted": self.quantidade_ted,
            "valor_ted": self.valor_ted,
            "quantidade_tec": self.quantidade_tec
        }