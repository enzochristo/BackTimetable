import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Booking(BaseModel):
    id: Optional[str]  # ID da reserva (opcional ao criar)
    customer_id: str   # ID do cliente que fez a reserva
    table_id: str      # ID da mesa reservada
    date: str          # Data da reserva (formato ISO: "YYYY-MM-DD")
    time: str          # Horário da reserva
    number_of_people: int