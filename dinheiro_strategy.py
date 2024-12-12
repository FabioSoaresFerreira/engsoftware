from pagamento_strategy import PagamentoStrategy

class DinheiroStrategy(PagamentoStrategy):



    def pagar(self, valor):
        
        print(f"Pagamento de R${valor} realizado com dinheiro")