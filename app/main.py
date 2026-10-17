from fastapi import FastAPI

from app.presentations.routers.user_router import router as user_router
from app.presentations.routers.profile_router import router as profile_router
from app.presentations.routers.task_router import router as task_router

app = FastAPI()


app.include_router(user_router)
app.include_router(profile_router)
app.include_router(task_router)