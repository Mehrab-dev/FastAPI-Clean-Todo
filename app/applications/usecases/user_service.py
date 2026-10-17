
from uuid import UUID

from app.domain.repositories.repositories import UserRepository
from app.domain.entities import entities
from app.shared.password import hash_password, verify_password
from app.shared.exceptions import ConflictError, ResourceNotFoundError, AuthenticationError


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository


    # /user/signup
    async def signup(
        self,
        *,
        payload: entities.User
    ) -> entities.User:
        payload.password = hash_password(payload.password)
        return await self.repository.create(payload=payload)


    # /users/login
    async def login(
        self,
        *,
        email: str,
        password: str
    ) -> entities.User:
        result = await self.repository.get_by_email(email=email)
        if result is None or not verify_password(password, result.password):
            raise AuthenticationError(
                message="incorrect email or password."
            )
        return result


    # /users/detail/by-id
    async def get_by_id(
        self,
        *,
        id: UUID
    ) -> entities.User | None:
        result = await self.repository.get_by_id(id=id)
        if result is None:
            raise ResourceNotFoundError(
                message="user with this id not found!"
            )
        return result


    # /users/update-email
    async def update_email(
        self,
        *,
        id: UUID,
        email: str
    ) -> entities.User | None:
        result = await self.repository.update_email_by_id(id=id, email=email)
        if result is None:
            raise ResourceNotFoundError(
                message="user with this id not found!"
            )
        return result


    # /users/update-password
    async def update_password(
        self,
        *,
        id: UUID,
        password: str
    ) -> bool:
        hashed_password = hash_password(password)
        result = await self.repository.update_password_by_id(id=id, new_password=hashed_password)
        if result is False:
            raise ResourceNotFoundError(
                message="user with this id not found!"
            )
        return True


    # /users/delete
    async def delete(
        self,
        *,
        id: UUID
    ) -> bool:
        result = await self.repository.delete(id=id)
        if result is False:
            raise ResourceNotFoundError(
                message="user with this id not found!"
            )
        return True