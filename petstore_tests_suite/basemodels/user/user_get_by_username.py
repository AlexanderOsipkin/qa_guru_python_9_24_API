from pydantic import BaseModel


class GetUserByUsernameResponse(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class GetRemoteUserByUsernameResponse(BaseModel):
    code: int
    type: str
    message: str
