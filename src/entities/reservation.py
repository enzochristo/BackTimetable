import dotenv
from pydantic import BaseModel
from typing import Literal
dotenv.load_dotenv()

class Reservation(BaseModel):
    _id: str
    table_id: int
    guests: int
    status: Literal ["scheduled", "available"]
    date : str
    time: str
