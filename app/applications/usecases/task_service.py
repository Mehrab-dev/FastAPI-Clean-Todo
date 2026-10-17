
from uuid import UUID
from typing import Any

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
        offset: int = 0,
        limit: int = 5,
        user_id: UUID
    ) -> list[entities.Task]:
        return await self.repository.list_tasks(user_id=user_id, offset=offset, limit=limit)


    # /tasks/list-by-status
    async def list_tasks_by_status(
        self,
        *,
        user_id: UUID,
        offset: int = 0,
        limit: int = 5,
        status: bool
    ) -> list[entities.Task]:
        return await self.repository.list_tasks_by_status(user_id=user_id, status=status, offset=offset, limit=limit)


    # /tasks/update
    async def update(
        self,
        *,
        user_id: UUID,
        task_id: UUID,
        payload: dict[str, Any]
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