
from abc import abstractmethod, ABC
from uuid import UUID

from app.domain.entities import entities



class UserRepository(ABC):

    @abstractmethod
    async def create(self, *, payload: entities.User) -> entities.User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, *, email: str) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, user_id: UUID) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, user_id: UUID, payload: entities.User) -> entities.User | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, user_id: UUID) -> bool:
        raise NotImplementedError



class ProfileRepository(ABC):

    @abstractmethod
    async def create(self, *, user_id: UUID) -> entities.Profile:
        raise NotImplementedError

    @abstractmethod
    async def get_by_userid(self, *, user_id: UUID) -> entities.Profile | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, user_id: UUID, payload: entities.Profile) -> entities.Profile | None:
        raise NotImplementedError



class TaskRepository(ABC):

    @abstractmethod
    async def create(self, *, user_id: UUID, payload: entities.Task) -> entities.Task:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, user_id: UUID, task_id: UUID) -> entities.Task | None:
        raise NotImplementedError

    @abstractmethod
    async def search_by_title(self, *, user_id: UUID, title: str) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def list_tasks(self, *, user_id: UUID) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def list_tasks_by_status(self, *, user_id: UUID, is_done: bool) -> list[entities.Task]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, user_id: UUID, task_id: UUID, payload: entities.Task) -> entities.Task | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, user_id: UUID, task_id: UUID) -> bool:
        raise NotImplementedError