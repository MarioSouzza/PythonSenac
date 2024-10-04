def obter_detalhes_pedidos():
    # Simula a obtenção de dados de um pedido
    pedido = {
        "item": "Notebook",
        "preco": 1200.00,
        "quantidade": 2
        }
    pedido2 = {
        "item2": "Mouse",
        "preco2": 200.00,
        "quantidade2": 5
    }
    print("Detalhes do pedido obtidos.")

    return pedido, pedido2


def calcular_preco_total(pedido1, pedido2):
    # Calcular o preço total do pedido
    preco_total = pedido1["preco"] * pedido1["quantidade"]
    preco_total2 = pedido2["preco2"] * pedido2["quantidade2"]

    print(f'Preço total calculado: R$ {preco_total + preco_total2:.2f}')
    
    
    return preco_total, preco_total2


def enviar_confirmacao(pedido1, preco_total1, pedido2, preco_total2):
    # Simula o envio de uma confrimação de pedido
    print(f"Confirmação enviada para {pedido1['quantidade']} {pedido1['item']}(s). ")
    print(f"Valor total a ser pago: R$ {preco_total1:.2f}")

    print(f"Confirmação enviada para {pedido2['quantidade2']} {pedido2['item2']}(s). ")
    print(f"Valor total a ser pago: R$ {preco_total2:.2f}")
  


def processar_pedido():
    # Chama as funções auxiliares para processar o pedido
    pedidos = obter_detalhes_pedidos()
    pedido1 = pedidos[0]
    pedido2 = pedidos[1]

    preco_total = calcular_preco_total(pedido1, pedido2)
    preco_total1 = preco_total[0]
    preco_total2 = preco_total[1]
    
    enviar_confirmacao(pedido1, preco_total1, pedido2, preco_total2)



# Chamando a função principal
processar_pedido()