
from uuid import UUID

from app.domain.repositories.repositories import TaskRepository
from app.domain.entities import entities


class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository


    # /tasks/create
    async def create(
        self,
        *,
        user_id: UUID,
        payload: entities.Task
    ) -> entities.Task:
        return await self.repository.create(user_id=user_id, payload=payload)


    # /tasks/title
    async def get_by_title(
        self,
        *,
        user_id: UUID,
        title: str
    ) -> list[entities.Task]:
        return await self.repository.get_by_title(user_id=user_id, title=title)


    # /tasks/list
    async def list_tasks(
        self,
        *,
        user_id: UUID
    ) -> list[entities.Task]:
        return await self.repository.list_tasks(user_id=user_id)


    # /tasks/list-by-status
    async def list_tasks_by_status(
        self,
        *,
        user_id: UUID,
        status: bool
    ) -> list[entities.Task]:
        return await self.repository.list_tasks_by_status(user_id=user_id, status=status)


    # /tasks/update
    async def update(
        self,
        *,
        user_id: UUID,
        task_id: UUID,
        payload: entities.Task
    ) -> entities.Task | None:
        return await self.repository.update(user_id=user_id, task_id=task_id, payload=payload)


    # /tasks/delete
    async def delete(
        self,
        *,
        user_id: UUID,
        task_id: UUID
    ) -> bool:
        return await self.repository.delete(user_id=user_id, task_id=task_id)