# Delivery-Comida-Vegana
 Sistema da  Loja Virtual - Comida Vegana Sim!


Estrutura
Sistema de Pedidos

- Customer
    name
    email

- Product
    name
    description
    price

- Order
    [OrderStatus]
    [OrderItem]
    total

- OrderSttus
    name (REALIZADO, EM PREPARAÇÂO, ENVIADO, ENTREGUE, FINALIZADO)

- OrderItem // objeto de valor -> imutável
    - product_id
    - price
    - quantity


