from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List


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
    
    model_config = ConfigDict(from_attributes=True)


class UserListSchema(BaseModel):
    items: List[UserSchema]
    