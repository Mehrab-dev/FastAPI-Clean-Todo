
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from uuid import UUID
from typing import Any

from app.domain.entities import entities
from app.infrastructure.database.models import TaskModel
from app.infrastructure.database.mappers import TaskMapper
from app.domain.repositories.repositories import TaskRepository




class SqlalchemyTaskRepository(TaskRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, *, user_id: UUID, payload: entities.Task) -> entities.Task:
        model = TaskMapper.to_model(entity=payload)
        model.user_id = user_id
        self.session.add(model)
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return TaskMapper.to_domain(model=model)


    async def get_by_title(self, *, user_id: UUID, title: str) -> list[entities.Task]:
        statement = select(TaskModel).where(
            TaskModel.user_id == user_id,
            TaskModel.title.ilike(f"%{title}%")
        )
        result = await self.session.execute(statement=statement)
        models = result.scalars().all()
        
        return  [TaskMapper.to_domain(model) for model in models]


    async def list_tasks(self, *, user_id: UUID, offset: int = 0, limit: int = 5) -> list[entities.Task]:
        statement = select(TaskModel).where(
            TaskModel.user_id == user_id
        ).offset(offset=offset).limit(limit=limit)
        result = await self.session.execute(statement=statement)
        models = result.scalars().all()

        return [TaskMapper.to_domain(model) for model in models]


    async def list_tasks_by_status(self, *, user_id: UUID, status: bool, offset: int = 0, limit: int = 5) -> list[entities.Task]:
        statement = select(TaskModel).where(
                TaskModel.user_id == user_id,
                TaskModel.status == status
        ).offset(offset=offset).limit(limit=limit)
        result = await self.session.execute(statement=statement)
        models = result.scalars().all()

        return [TaskMapper.to_domain(model) for model in models]


    async def update(self, *, user_id: UUID, task_id: UUID, payload: dict[str, Any]) -> entities.Task | None:
        statement = select(TaskModel).where(
            TaskModel.user_id == user_id,
            TaskModel.id == task_id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        for field, value in payload.items():
            if field in {"title", "description", "status"}:
                setattr(model, field, value)
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return TaskMapper.to_domain(model=model)


    async def delete(self, *, user_id: UUID, task_id: UUID) -> bool:
        statement = select(TaskModel).where(
            TaskModel.user_id == user_id,
            TaskModel.id == task_id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return False
        try:
            await self.session.delete(model)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return True