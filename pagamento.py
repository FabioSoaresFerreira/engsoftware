from pagamento_strategy import PagamentoStrategy
from cartao_credito_strategy import CartaoCreditoStrategy
from debito_strategy import DebitoStrategy

from dinheiro_strategy import DinheiroStrategy




class Pagamento:
    def __init__(self, strategy: PagamentoStrategy):


        self.strategy = strategy

    def realizar_pagamento(self, valor):
        self.strategy.pagar(valor)

