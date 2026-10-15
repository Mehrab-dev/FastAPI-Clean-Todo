from fastapi import APIRouter, status, HTTPException, Depends

from uuid import UUID


router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/detail-by-id")
async def get_by_id():
    pass


@router.get("/get-by-userid")
async def get_by_user_id():
    pass


@router.put("/update")
async def update():
    pass