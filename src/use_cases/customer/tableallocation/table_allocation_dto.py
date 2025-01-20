from pydantic import BaseModel, EmailStr

class CreateBookingDTO(BaseModel):
    email: str         # E-mail do cliente (identificador)
    date: str               # Data da reserva (formato ISO: "YYYY-MM-DD")
    time: str               # Horário da reserva
    number_of_people: int   # Número de pessoas para a reserva
