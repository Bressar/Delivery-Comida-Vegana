from pydantic import BaseModel, Field
from src.domain.base import DomainBase
from uuid import UUID, uuid4 
from src.domain.customer import Customer

from enum import Enum # enumerations (ou enums), tipos de dados que consistem em um conjunto de valores simbólicos nomeados. Enum é útil quando para representar um conjunto fixo de opções ou estados que não devem ser modificados durante a execução do programa, melhorando a legibilidade e a manutenção do código.


class OrderStatusName(str, Enum):
    # Enum pata definir estados fixos: representar estados em uma máquina de estados, como PENDING, IN_PROGRESS, e COMPLETED em um fluxo de trabalho.
    ACCOMPLISHED = 'realizado'
    IN_PREPARATION = 'em preparação'
    SENT = 'enviado'
    DELIVERED = 'entregue'
    FINISHED = 'finalizado'


class OrderStatus(DomainBase):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED) # por padrão realizado (já que o pedido foi feito)
    # realizado, em preparação, enviado, entregue, finalizado
    
    
class OrderItem(DomainBase):
    product_id: UUID
    price: float
    quantity: int


class Order(DomainBase):
    customer: Customer # sem cliente não tem pedido!!
    status: list[OrderStatus] = Field(default=[]) # Iniciam como listas vazias
    items: list[OrderItem] = Field(default=[])
    
    def add_status(self, status: OrderStatus):
        self.status.append(status)
        
    def add_item(self, item: OrderItem):
        self.items.append(item)
        
    def total(self):
        return sum([item.price * item.quantity for item in self.items]) 
