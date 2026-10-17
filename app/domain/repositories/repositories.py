
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Any

from app.domain.entities import entities



class UserRepository(ABC):
    
    @abstractmethod
    async def create(self, *, payload: entities.User) -> entities.User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, id: UUID) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, *, email: str) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def update_email_by_id(self, *, id: UUID, email: str) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def update_password_by_id(self, *, id: UUID, new_password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, id: UUID) -> bool:
        raise  NotImplementedError



class ProfileRepository(ABC):

    @abstractmethod
    async def create(self, *, user_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, id: UUID) -> entities.Profile | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_user_id(self, *, user_id: UUID) -> entities.Profile | None:
        raise NotImplementedError

    @abstractmethod
    async def update(
        self, 
        *, 
        user_id: UUID, 
        first_name: str | None = None,
        last_name: str | None = None,
        bio: str | None = None,
        image: str | None = None
    ) -> entities.Profile | None:
        raise NotImplementedError



class TaskRepository(ABC):

    @abstractmethod
    async def create(self, *, user_id: UUID, payload: entities.Task) -> entities.Task:
        raise NotImplementedError

    @abstractmethod
    async def get_by_title(self, *, user_id: UUID, title: str) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def list_tasks(self, *, user_id: UUID, offset: int = 0, limit: int =5,) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def list_tasks_by_status(self, *, user_id: UUID, status: bool, offset: int = 0, limit: int = 5) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, user_id: UUID, task_id: UUID, payload: dict[str, Any]) -> entities.Task | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, user_id: UUID, task_id: UUID) -> bool:
        raise NotImplementedError