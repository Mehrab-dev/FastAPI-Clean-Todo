
from abc import ABC, abstractmethod

from uuid import UUID

from app.domain.entities.entities import User, Profile, Task


class UserRepository(ABC):
    @abstractmethod
    async def create(self, *, payload: User) -> User:
        ...

    @abstractmethod
    async def get_by_id(self, *, user_id: UUID) -> User | None:
        ...

    @abstractmethod
    async def get_by_email(self, *, email: str) -> User | None:
        ...

    @abstractmethod
    async def update(self, *, user_id: UUID, payload: User) -> User | None:
        ...

    @abstractmethod
    async def delete(self, *, user_id: UUID) -> bool:
        ...



class ProfileRepository(ABC):
    @abstractmethod
    async def create(self, *, user_id: UUID) -> Profile:
        ...

    @abstractmethod
    async def get_by_user_id(self, *, user_id: UUID) -> Profile | None:
        ...

    @abstractmethod
    async def update(self, *, user_id: UUID, payload: Profile) -> Profile | None:
        ...



class TaskRepository(ABC):
    @abstractmethod
    async def create(self, *, user_id: UUID,  payload: Task) -> Task:
        ...

    @abstractmethod
    async def get_by_id(self, *, user_id: UUID, task_id: UUID) -> Task | None:
        ...

    @abstractmethod
    async def search_by_title(self, *, user_id: UUID, query: str) -> list[Task]:
        ...

    @abstractmethod
    async def list_tasks(self, *, user_id: UUID) -> list[Task]:
        ...

    @abstractmethod
    async def list_tasks_by_complete(self, *, user_id: UUID, complete: bool) -> list[Task]:
        ...

    @abstractmethod
    async def update(self, *, user_id: UUID, task_id: UUID, payload: Task) -> Task | None:
        ...

    @abstractmethod
    async def delete(self, *, user_id: UUID, task_id: UUID) -> bool:
        ...