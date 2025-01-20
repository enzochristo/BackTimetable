from pydantic import BaseModel

class CreateBookingManagerDTO(BaseModel):
    date: str
    time: str
    number_of_people: int
    table_id: str  # ID da mesa selecionada pelo gerente
