from pydantic import BaseModel
from typing import Literal, Optional


class CreateBookingDTO(BaseModel):
    date: str          # Data da reserva (formato ISO: "YYYY-MM-DD")
    time: str          # Horário da reserva
    number_of_people: int
    email : str
