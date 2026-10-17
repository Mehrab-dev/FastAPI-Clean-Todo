from fastapi import APIRouter, status, HTTPException, Depends, UploadFile, File

from uuid import UUID

from app.presentations.schemas.profile_schemas import ProfileResponseSchema, ProfileUpdateSchema
from app.presentations.dependencies import get_profile_service
from app.applications.usecases.profile_service import ProfileService


router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/detail-by-id", response_model=ProfileResponseSchema, status_code=status.HTTP_200_OK)
async def get_by_id(
    *,
    id: UUID,
    service: ProfileService = Depends(get_profile_service)
):
    return await service.get_by_id(id=id)


@router.get("/get-by-userid", response_model=ProfileResponseSchema, status_code=status.HTTP_200_OK)
async def get_by_user_id(
    *,
    user_id: UUID,
    service: ProfileService = Depends(get_profile_service)
):
    return await service.get_by_user_id(user_id=user_id)


@router.put("/update", response_model=ProfileResponseSchema, status_code=status.HTTP_200_OK)
async def update(
    *,
    user_id: UUID,
    payload: ProfileUpdateSchema,
    image: UploadFile = File(...),
    service: ProfileService = Depends(get_profile_service)
):
    return await service.update(
        user_id=user_id,
        first_name=payload.first_name,
        last_name=payload.last_name,
        bio=payload.bio,
        image=image
    )