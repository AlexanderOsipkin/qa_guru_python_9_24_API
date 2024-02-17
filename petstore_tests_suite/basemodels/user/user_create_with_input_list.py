import json

from typing import List
from pydantic import BaseModel
from petstore_tests_suite.utils import random_data


class UserData(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class CreateUserWithInputListRequest(BaseModel):
    __root__: List[UserData]


class CreateUserWithInputListResponse(BaseModel):
    code: int
    type: str
    message: str


input_json = json.dumps(
    [
        {
            "id": random_data.user_id(),
            "username": random_data.username(),
            "firstName": random_data.first_name(),
            "lastName": random_data.last_name(),
            "email": random_data.email(),
            "password": random_data.password(),
            "phone": random_data.phone(),
            "userStatus": 0,
        },
        {
            "id": random_data.user_id(),
            "username": random_data.username(),
            "firstName": random_data.first_name(),
            "lastName": random_data.last_name(),
            "email": random_data.email(),
            "password": random_data.password(),
            "phone": random_data.phone(),
            "userStatus": 0,
        },
    ]
)
