
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime  import datetime

from app.shared.datetime import utc_now


@dataclass(kw_only=True)
class User:
    id: UUID = field(default_factory=uuid4)
    email: str
    password: str
    is_active: bool = True
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def _touch(self) -> None:
        self.updated_at = utc_now()

    def deactivate(self) -> None:
        self.is_active = False
        self._touch()

    def change_password(self, new_password: str) -> None:
        self.password = new_password
        self._touch()

    def change_email(self, new_email: str) -> None:
        self.email = new_email
        self._touch()



@dataclass(kw_only=True)
class Profile:
    id: UUID = field(default_factory=uuid4)
    user_id: UUID
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None
    image: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def _touch(self) -> None:
        self.updated_at = utc_now()

    def update_info(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        bio: str | None = None,
        image: str | None = None
    ) -> None:
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if bio is not None:
            self.bio = bio
        if image is not None:
            self.image = image
        self._touch()




@dataclass(kw_only=True)
class Task:
    id: UUID = field(default_factory=uuid4)
    user_id: UUID
    title: str
    description: str | None = None
    is_done: bool = False
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def _touch(self) -> None:
        self.updated_at = utc_now()

    def update_info(
        self,
        title: str | None = None,
        description: str | None = None,
        is_done: bool | None = None
    ) -> None:
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if is_done is not None:
            self.is_done = is_done
        self._touch()