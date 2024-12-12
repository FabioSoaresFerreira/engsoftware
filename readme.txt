No programa temos 6 arquivos Python, onde 5 sao classes. Temo as classes:
cartao_credito_strategy, debito_strategy, dinheiro_strategy, pagamento e pagamento_strategy.
No arquivo pagamento_strategy foi definida a interface PagamentoStrategy que define o método pagar(valor)

No arquivo cartao_credito_strategy definimos a classe CartaoCreditoStrategy que implementa a interface PagamentoStrategy
A classe CartaoCresditoStrategy cria o metodo pagar(valor) que realiza o pagamento com cartao de crédito

No arquivo debito_strategy.py, definimos a classe DebitoStrategy que implementa a interface PagamentoStrategy.

A classe DebitoStrategy define o método pagar(valor) que realiza o pagamento com débito.

No arquivo dinheiro_strategy.py, definimos a classe DinheiroStrategy que implementa a interface PagamentoStrategy.
A classe DinheiroStrategy define o método pagar(valor) que realiza o pagamento com dinheiro.
-------------------------------------------------------------------------------------------
No arquivo pagamento.py, definimos a classe Pagamento que utiliza a interface PagamentoStrategy.
A classe Pagamento define o método realizar_pagamento(valor) que chama o método pagar(valor) da estratégia de pagamento associada.

No arquivo main.py, criamos instâncias das estratégias de pagamento (CartaoCreditoStrategy, DebitoStrategy e DinheiroStrategy).
Criamos instâncias da classe Pagamento e associamos cada instância a uma estratégia de pagamento específica.
Chamamos o método realizar_pagamento(valor) da classe Pagamento para realizar o pagamento com a estratégia de pagamento associada.

---------------------------------------------------------------------------------------------
O método Strategy está aplicado na classe Pagamento, que utiliza a interface PagamentoStrategy para definir o comportamento de pagamento.
A classe Pagamento não sabe qual é a estratégia de pagamento específico que está sendo utilizada, apenas sabe que deve chamar o método pagar(valor) da estratégia de pagamento associada.
Isso permite que a classe Pagamento seja independente das estratégias de pagamento específicas e que possamos adicionar novas estratégias de pagamento sem modificar a classe Pagamento.