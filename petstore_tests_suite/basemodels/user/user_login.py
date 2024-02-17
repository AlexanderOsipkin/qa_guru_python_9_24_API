from pydantic import BaseModel


class UserLoginResponse(BaseModel):
    code: int
    type: str
    message: str
