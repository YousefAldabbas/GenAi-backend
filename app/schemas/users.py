from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    full_name: str
    date_of_birth: str
    email: EmailStr
    phone_number: str

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class UserIn(UserBase):
    password: str


class UserUpdate(BaseModel):

    full_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None


class UserOut(UserBase):
    id: int
    done_ekyc: bool
