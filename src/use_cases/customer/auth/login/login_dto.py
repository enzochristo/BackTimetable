from pydantic import BaseModel,ConfigDict
from typing import Literal

class LoginDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")


    email: str
    password: str
