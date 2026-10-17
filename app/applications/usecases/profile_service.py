
from fastapi import UploadFile

from uuid import UUID

from app.domain.repositories.repositories import ProfileRepository
from app.domain.entities import entities
from app.shared.filestorage import save_profile_image
from app.shared.exceptions import ResourceNotFoundError



class ProfileService:

    def __init__(self, repository: ProfileRepository):
        self.repository = repository


    async def create(
        self,
        *,
        user_id: UUID
    ) -> None:
        await self.repository.create(user_id=user_id)


    # /profiles/detail-by-id
    async def get_by_id(
        self,
        *,
        id: UUID
    ) -> entities.Profile | None:
        result =  await self.repository.get_by_id(id=id)
        if result is None:
            raise ResourceNotFoundError(
                message="profile with this id not found!"
            )
        return result


    # /profiles/get-by-userid
    async def get_by_user_id(
        self,
        *,
        user_id: UUID
    ) -> entities.Profile | None:
        result = await self.repository.get_by_user_id(user_id=user_id)
        if result is None:
            raise ResourceNotFoundError(
                message="profile with this user_id not found!"
            )
        return result


    # /profiles/update
    async def update(
        self,
        *,
        user_id: UUID,
        first_name: str | None = None,
        last_name: str | None = None,
        bio: str | None = None,
        image: UploadFile | None = None
    ) -> entities.Profile | None:
        image_path = None
        if image is not None:
            image_path = await save_profile_image(image)
       
        result = await self.repository.update(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            image=image_path
        )

        if result is None:
            raise ResourceNotFoundError(
                message="profile with this user_id not found!"
            )
        return result