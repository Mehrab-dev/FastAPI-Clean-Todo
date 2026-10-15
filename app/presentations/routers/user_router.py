from fastapi import APIRouter, HTTPException, status, Depends


router = APIRouter(prefix="/users", tags=["users"])



@router.post("/signup")
async def signup():
    pass


@router.post("/login")
async def login():
    pass


@router.get("/detail/by-id")
async def get_by_id():
    pass


@router.patch("/update-email")
async def update_email():
    pass


@router.patch("/update-password")
async def update_password():
    pass


@router.delete("/delete")
async def delete():
    pass