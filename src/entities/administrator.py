import dotenv
from pydantic import BaseModel, EmailStr
from typing import Literal
dotenv.load_dotenv()

class Administrator(BaseModel):
    _id: str
    name: str
    email: EmailStr
    password: str
