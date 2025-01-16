import dotenv
from pydantic import BaseModel, EmailStr
from typing import Optional
dotenv.load_dotenv()

class Customer(BaseModel):
    _id: str
    name: str
    email: EmailStr
    password: str
    phone: Optional[str]
