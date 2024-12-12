from pagamento_strategy import PagamentoStrategy

class DebitoStrategy(PagamentoStrategy):

    def __init__(self, numero_conta, agencia):

        self.numero_conta = numero_conta
        self.agencia = agencia



    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com débito da conta {self.numero_conta} da agência {self.agencia}")