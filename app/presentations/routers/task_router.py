from fastapi import APIRouter, status, Depends, Query, HTTPException

from uuid import UUID

from app.presentations.schemas.task_schemas import TaskCreateSchema, TaskUpdateSchema, TaskResponseSchema
from app.applications.usecases.task_service import TaskService
from app.presentations.dependencies import get_task_service
from app.domain.entities import entities



router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
async def create(
    *,
    user_id: UUID,
    payload: TaskCreateSchema,
    service: TaskService = Depends(get_task_service)
):
    domain_payload = entities.Task(
        user_id=user_id,
        title=payload.title,
        description=payload.description,
    )
    return await service.create(user_id=user_id, payload=domain_payload)



@router.get("/title", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK)
async def get_by_title(
    *,
    user_id: UUID,
    title: str,
    service: TaskService = Depends(get_task_service)
):
    return await service.get_by_title(user_id=user_id, title=title)



@router.get("/list", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK)
async def list_tasks(
    *,
    user_id: UUID,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=5, gt=0, le=20),
    service: TaskService = Depends(get_task_service)
):
    return await service.list_tasks(user_id=user_id, offset=offset, limit=limit)



@router.get("/list-by-status", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK)
async def list_tasks_by_status(
    *,
    user_id: UUID,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=5, gt=0, le=20),
    status: bool,
    service: TaskService = Depends(get_task_service)
):
    return await service.list_tasks_by_status(user_id=user_id, status=status, offset=offset, limit=limit)



@router.patch("/update", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
async def update(
    *,
    user_id: UUID,
    task_id: UUID,
    payload: TaskUpdateSchema,
    service: TaskService = Depends(get_task_service)
):
    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field must be provided."
        )
    return await service.update(
        user_id=user_id,
        task_id=task_id,
        payload=updates
    )



@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    *,
    user_id: UUID,
    task_id: UUID,
    service: TaskService = Depends(get_task_service)
):
    await service.delete(user_id=user_id, task_id=task_id)