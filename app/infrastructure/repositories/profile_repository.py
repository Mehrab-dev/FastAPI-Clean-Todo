
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from app.domain.repositories.repositories import ProfileRepository
from app.infrastructure.database.models import ProfileModel
from app.infrastructure.database.mappers import ProfileMapper
from app.domain.entities import entities



class SqlalchemyProfileRepository(ProfileRepository):

    def __init__(self, session: AsyncSession):
        self.session = session


    async def create(self, *, user_id: UUID) -> None:
        model = ProfileModel(user_id=user_id)
        self.session.add(model)
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise


    async def get_by_id(self, *, id: UUID) -> entities.Profile | None:
        statement = select(ProfileModel).where(
            ProfileModel.id == id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return ProfileMapper.to_domain(model=model)


    async def get_by_user_id(self, *, user_id: UUID) -> entities.Profile | None:
        statement = select(ProfileModel).where(
            ProfileModel.user_id == user_id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return ProfileMapper.to_domain(model=model)


    async def update(
        self,
        *,
        user_id: UUID,
        first_name: str | None = None,
        last_name: str | None = None,
        bio: str | None = None,
        image: str | None = None
    ) -> entities.Profile | None:
        statement = select(ProfileModel).where(
            ProfileModel.user_id == user_id
        )
        result = await self.session.execute(statement=statement)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        model.first_name = first_name
        model.last_name = last_name
        model.bio = bio
        model.image = image
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return ProfileMapper.to_domain(model=model)