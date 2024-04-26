from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributese=True, arbitrary_types_allowed=True)


class UserIn(UserBase):
    ...


class UserUpdate(UserBase):
    ...


class UserOut(BaseModel):
    username: str
    email: EmailStr

    class Config:
        from_attributese = True
