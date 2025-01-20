from pydantic import BaseModel, EmailStr
from typing import Optional

class WaitList(BaseModel):
    id: Optional[str]  # ID da entrada na lista de espera (gerado automaticamente)
    customer_email: EmailStr  # E-mail do cliente
    date: str               # Data da tentativa de reserva
    time: str               # Horário da tentativa de reserva
    number_of_people: int   # Número de pessoas na tentativa
    priority: int           # Prioridade na fila (1 = mais alta, 2, 3, ...)
