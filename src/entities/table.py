import dotenv
from pydantic import BaseModel
from typing import Optional,Literal
dotenv.load_dotenv()

class Table(BaseModel):
    _id_table: str
    _id_reservation: Optional[str] = None
    cadeiras: int
    status: Literal["available","ocupied"]
    



