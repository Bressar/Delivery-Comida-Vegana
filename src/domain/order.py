from pydantic import BaseModel

class OrderStatus(BaseModel):
    name: str # realizado, em preparação, enviado, entregue, finalizado
    
class OrderItem(BaseModel):
    product_id: int
    price: float
    quantity: int

class Order(BaseModel):
    status: list[OrderStatus] = Field(default=[]) # Iniciam como listas vazias
    items: list[OrderItem] = Field(default=[])
