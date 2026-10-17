
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.repositories.user_repository import SqlalchemyUserRepository
from app.infrastructure.repositories.profile_repository import SqlalchemyProfileRepository
from app.infrastructure.repositories.task_repository import SqlalchemyTaskRepository

from app.applications.usecases.task_service import TaskService
from app.applications.usecases.user_service import UserService
from app.applications.usecases.profile_service import ProfileService

from app.infrastructure.database.session import get_database_session


def get_user_service(session: AsyncSession = Depends(get_database_session)):
    repository = SqlalchemyUserRepository(session=session)
    return UserService(repository=repository)


def get_profile_service(session: AsyncSession = Depends(get_database_session)):
    repository = SqlalchemyProfileRepository(session=session)
    return ProfileService(repository=repository)


def get_task_service(session: AsyncSession = Depends(get_database_session)):
    repositpry = SqlalchemyTaskRepository(session=session)
    return TaskService(repository=repositpry)