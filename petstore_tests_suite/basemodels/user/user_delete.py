from pydantic import BaseModel


class DeleteUserResponse(BaseModel):
    code: int
    type: str
    message: str
