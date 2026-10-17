
from pydantic import BaseModel, Field

from typing import Optional
from uuid import UUID

from datetime import datetime, timezone



def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class TaskCreateSchema(BaseModel):
    title: str = Field(..., max_length=255, description="title of the task")
    description: Optional[str] = Field(None, max_length=600, description="description of the task")


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="title of the task of the task for update")
    description: Optional[str] = Field(None, max_length=600, description="description of the task for update")
    status: Optional[bool] = Field(None, description="state of the task for update")


class TaskResponseSchema(BaseModel):
    title: str
    description: Optional[str]
    status: bool
    created_at: datetime
    updated_at: datetime