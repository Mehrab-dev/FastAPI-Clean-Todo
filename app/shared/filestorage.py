
from fastapi import UploadFile

from pathlib import Path
from uuid import uuid4


UPLOAD_DIR = Path("uploads/profiles")


async def save_profile_image(file: UploadFile) -> str:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    extentions = Path(file.filename or "").suffix.lower()
    filename = f"{uuid4().hex}{extentions}"
    filepath = UPLOAD_DIR / filename

    return filepath.as_posix()