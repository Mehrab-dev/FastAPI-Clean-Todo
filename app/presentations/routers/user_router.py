from fastapi import APIRouter, status, Depends

from uuid import UUID

from app.presentations.dependencies import get_user_service
from app.applications.usecases.user_service import UserService
from app.domain.entities import entities
from app.presentations.schemas.user_schemas import (UserSignUpSchema, UserLoginSchema,
                                                    UserUpdateEmailSchema, UserUpdatePasswordSchema, UserResponseSchema)



router = APIRouter(prefix="/users", tags=["users"])



@router.post("/signup", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def signup(
    *,
    payload: UserSignUpSchema,
    service: UserService = Depends(get_user_service)
):
    domain_payload = entities.User(
        email=payload.email,
        password=payload.password
    )
    return await service.signup(payload=domain_payload)



@router.post("/login", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def login(
    *,
    payload: UserLoginSchema,
    service: UserService = Depends(get_user_service)
):
    return await service.login(email=payload.email, password=payload.password)



@router.get("/detail/by-id", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_by_id(
    *,
    id: UUID,
    service: UserService = Depends(get_user_service)
):
    return await service.get_by_id(id=id)
    


@router.patch("/update-email", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def update_email(
    *,
    id: UUID,
    payload: UserUpdateEmailSchema,
    service: UserService = Depends(get_user_service)
):
    return await service.update_email(id=id, email=payload.email)



@router.patch("/update-password", status_code=status.HTTP_200_OK)
async def update_password(
    *,
    id: UUID,
    payload: UserUpdatePasswordSchema,
    service: UserService = Depends(get_user_service)
):
    return await service.update_password(id=id, password=payload.new_password)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    *,
    id: UUID,
    service: UserService = Depends(get_user_service)
):
    return await service.delete(id=id)