from pydantic import BaseModel, ConfigDict


class EkycBase(BaseModel):
    ...
    model_config = ConfigDict(from_attributese=True, arbitrary_types_allowed=True)


class EkycIn(EkycBase):
    ...


class EkycUpdate(EkycBase):
    ...


class EkycOut(BaseModel):
    ...
