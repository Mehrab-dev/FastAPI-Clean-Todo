
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from uuid import UUID

from app.domain.repositories.repositories import UserRepository
from app.domain.entities import entities
from app.infrastructure.database.models import UserModel
from app.infrastructure.database.mappers import UserMapper
from app.shared.exceptions import ConflictError



class SqlalchemyUserRepository(UserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session


    async def create(self, *, payload: entities.User) -> entities.User:
        model = UserMapper.to_model(entity= payload)
        self.session.add(model)
        try:
            await self.session.commit()
        except IntegrityError as exc:
            await self.session.rollback()
            raise ConflictError(
                message="user with this email already exists."
            ) from exc
        return UserMapper.to_domain(model=model)


    async def get_by_id(self, *, id: UUID) -> entities.User | None:
        statement = select(UserModel).where(
            UserModel.id == id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None

        return UserMapper.to_domain(model=model)


    async def get_by_email(self, *, email: str) -> entities.User | None:
        statement = select(UserModel).where(
            UserModel.email == email
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return UserMapper.to_domain(model=model)


    async def update_email_by_id(self, *, id: UUID, email: str) -> entities.User | None:
        statement = select(UserModel).where(
            UserModel.id == id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None

        model.email = email
        try:
            await self.session.commit()
        except IntegrityError as exc:
            await self.session.rollback()
            raise ConflictError(
                message="user with this email already exists."
            ) from exc
        return UserMapper.to_domain(model=model)


    async def update_password_by_id(self, *, id: UUID, new_password: str) -> bool:
        statement = select(UserModel).where(
            UserModel.id == id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return False

        model.password = new_password
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return True


    async def delete(self, *, id: UUID) -> bool:
        statement = select(UserModel).where(
            UserModel.id == id
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