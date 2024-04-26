from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

    model_config = ConfigDict(orm_mode=True, arbitrary_types_allowed=True)


class UserIn(UserBase):
    ...


class UserUpdate(UserBase):
    ...


class UserOut(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
