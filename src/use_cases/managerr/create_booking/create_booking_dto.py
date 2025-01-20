from pydantic import BaseModel, EmailStr
from typing import Literal, Optional

class CreateBookingDTO(BaseModel):
    email: str    # E-mail do cliente (identificador principal)
    date: str          # Data da reserva (formato ISO: "YYYY-MM-DD")
    time: str          # Horário da reserva
    number_of_people: int
