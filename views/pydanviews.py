from pydantic.main import BaseModel


class Orderview(BaseModel):
    productname: str
    emailId: str

    class Config:
        orm_mode = True