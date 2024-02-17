from pydantic import BaseModel


class UserLogOutResponse(BaseModel):
    code: int
    type: str
    message: str
