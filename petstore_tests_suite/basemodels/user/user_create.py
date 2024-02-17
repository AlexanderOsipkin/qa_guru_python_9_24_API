import json

from pydantic import BaseModel
from petstore_tests_suite.utils import random_data


class CreateUserRequest(BaseModel):
    id: int = 0
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class CreateUserResponse(BaseModel):
    code: int
    type: str
    message: str


input_json = json.dumps(
    {
        "id": random_data.user_id(),
        "username": random_data.username(),
        "firstName": random_data.first_name(),
        "lastName": random_data.last_name(),
        "email": random_data.email(),
        "password": random_data.password(),
        "phone": random_data.phone(),
        "userStatus": 0,
    }
)
