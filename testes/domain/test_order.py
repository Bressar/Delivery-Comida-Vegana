from src.domain.order import Order, OrderStatus, OrderStatusName, OrderItem
from src.domain.product import Product
from src.domain.customer import Customer


def test_should_create_order():  
    customer: Customer = Customer(name="Douglas", email="bressar@bessar.com")
    
    status: OrderStatus = OrderStatus()
    
    assert status.name == OrderStatusName.ACCOMPLISHED # verifica por padrão se o pedido foi realizado
    
    product1: Product = Product(name="Feijoada", description="Feijoada Vegana", price=30)
    
    assert product1.name == "Feijoada"
    assert product1.description == "Feijoada Vegana"
    assert product1.price == 30.0
    
    
    product2: Product = Product(name="Escondidinho", description="Escondidinho de carne de jaca", price=28.5)
    
    assert product2.name == "Escondidinho"
    assert product2.description == "Escondidinho de carne de jaca"
    assert product2.price == 28.5
    
    item1: OrderItem = OrderItem(
        product_id=product1.id, price=product1.price, quantity=1
        )
    item2: OrderItem = OrderItem(
        product_id=product2.id, price=product2.price, quantity=2
        )
    
    
    order =  Order(customer = customer)  # igual a order: Order = Order()
    order.add_status(status)
    order.add_item(item1)
    order.add_item(item2)
    
    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED  # Enum correto
    assert len(order.items) == 2
    
    # novo status: em preparação
    status2 = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status2)
    
    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.IN_PREPARATION
    
    # novo status: enviado
    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status3)
    
    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SENT
    
    # novo status: entregue
    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)
    
    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED
    
    # novo status: finalizado
    status5 = OrderStatus(name=OrderStatusName.FINISHED)
    order.add_status(status5)
    
    assert len(order.status) == 5
    assert order.status[4].name == OrderStatusName.FINISHED
      
    # verificando Total 
    assert order.total() == 87.0 # feijoada $30, escondidinho 2X 28,5
    
    # Fluxo verificado!