from pydantic import BaseModel, Field
from src.domain.base import DomainBase

class OrderStatus(DomainBase):
    name: str # realizado, em preparação, enviado, entregue, finalizado
    
class OrderItem(DomainBase):
    product_id: int
    price: float
    quantity: int

class Order(DomainBase):
    status: list[OrderStatus] = Field(default=[]) # Iniciam como listas vazias
    items: list[OrderItem] = Field(default=[])
