from datetime import datetime
from typing import List
from pydantic import BaseModel


class TestBaseSchema(BaseModel):
    id: str | None = None
    name: str
    description: str
    category: str
    published: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class UserBaseSchema(BaseModel):
    id: str | None = None
    first_name: str
    last_name: str
    email: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListTestResponse(BaseModel):
    status: str
    tests: List[TestBaseSchema]


class ListUserResponse(BaseModel):
    status: str
    tests: List[UserBaseSchema]
