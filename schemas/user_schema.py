from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreateSchema(BaseModel):
    name: str
    surname: str
    email: EmailStr
    age: int
    

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    
    
class UserSchema(UserCreateSchema):
    id: int
    
    class Config:
        from_atributes = True
