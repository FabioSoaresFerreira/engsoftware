from pagamento_strategy import PagamentoStrategy

class CartaoCreditoStrategy(PagamentoStrategy):
    
    def __init__(self, numero_cartao, validade, cvv):

        self.numero_cartao = numero_cartao

        self.validade = validade
        self.cvv = cvv

    def pagar(self, valor):

        print(f"Pagamento de R${valor} realizado com cartão de crédito {self.numero_cartao}")