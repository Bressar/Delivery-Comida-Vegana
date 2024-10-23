from uuid import UUID, uuid4 # UIDs (Universally Unique Identifiers) o uuid4 gera um id aleatório -> ex.: b59b58f3-522a-40ff-857a-c6a42dbfd979
""" UUIDs são comumente utilizados em contextos como:
    - Identificadores únicos em bancos de dados distribuídos.
    - Identificadores únicos em APIs.
    - Garantia de que os IDs gerados por diferentes sistemas não entrem em conflito """
    
from pydantic import BaseModel, Field
from datetime import datetime

class DomainBase(BaseModel): # cria um Id e uma date time toda vez que a classe for instanciada
    id: UUID = Field(default=uuid4())
    create_at: datetime = Field(default_factory=datetime.now)