
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional



class ProfileResponseSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    bio: Optional[str]
    image: Optional[str]


class ProfileUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(None, max_length=255, description="first name of the user")
    last_name: Optional[str] = Field(None, max_length=255, description="last name of the user")
    bio: Optional[str] = Field(None, max_length=600, description="description of the user")
    