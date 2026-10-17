from pydantic import BaseModel, Field, field_validator, EmailStr, ValidationInfo
from typing import Optional

from uuid import UUID
from datetime import datetime, timezone



class UserSignUpSchema(BaseModel):
    email: EmailStr = Field(..., description="email of the user for signup")
    password: str = Field(..., description="password of the user for signup")
    confirm_password: str = Field(..., description="confirm password of the user for signup")

    @field_validator("confirm_password")
    @classmethod
    def check_match_password(cls, confirm_password, info: ValidationInfo) -> str:
        if (confirm_password != info.data.get("password")):
            raise ValueError("password was not match")
        return confirm_password


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(..., description="email of the user for login")
    password: str = Field(..., description="password of the user for login")


class UserUpdateEmailSchema(BaseModel):
    email: EmailStr = Field(..., description="email of the user for update")


class UserUpdatePasswordSchema(BaseModel):
    new_password: str = Field(..., description="new password of the user for update password")
    confirm_new_password: str = Field(..., description="confirm new password of the user for update password")

    @field_validator("confirm_new_password")
    @classmethod
    def check_match_password(cls, confirm_new_password, info: ValidationInfo) -> str:
        if (confirm_new_password != info.data.get("new_password")):
            raise ValueError("password was not match")
        return confirm_new_password


class UserResponseSchema(BaseModel):
    email: EmailStr
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime