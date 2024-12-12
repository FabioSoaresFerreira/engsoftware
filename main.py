from pagamento import Pagamento
from cartao_credito_strategy import CartaoCreditoStrategy

from debito_strategy import DebitoStrategy
from dinheiro_strategy import DinheiroStrategy


if __name__ == "__main__":

   
    cartao_credito = CartaoCreditoStrategy("1234-5678-9012-3456", "12/2025", "123")
    debito = DebitoStrategy("1234567890", "1234")

    dinheiro = DinheiroStrategy()

   
    pagamento_cartao_credito = Pagamento(cartao_credito)
    pagamento_debito = Pagamento(debito)


    pagamento_dinheiro = Pagamento(dinheiro)




    pagamento_cartao_credito.realizar_pagamento(100)
    
    pagamento_dinheiro.realizar_pagamento(50)

    