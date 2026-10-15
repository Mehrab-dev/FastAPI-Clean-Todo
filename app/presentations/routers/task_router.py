from fastapi import APIRouter, status, HTTPException, Depends


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/create")
async def create():
    pass


@router.get("/title")
async def get_by_title():
    pass


@router.get("/list")
async def list_tasks():
    pass


@router.get("/list-by-status")
async def list_tasks_by_status():
    pass


@router.patch("/update")
async def update():
    pass


@router.delete("/delete")
async def delete():
    pass