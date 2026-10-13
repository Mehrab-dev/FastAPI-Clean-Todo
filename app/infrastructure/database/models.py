from sqlalchemy import String, Text, DateTime, ForeignKey, Boolean, UUID as uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.infrastructure.database.base import Base

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, default=uuid4, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationships """
    profile = relationship("ProfileModel", back_populates="user", uselist=False, cascade="all, delete-orphan")
    tasks = relationship("TaskModel", back_populates="user", cascade="all, delete-orphan")



class ProfileModel(Base):
    __tablename__ = "profiles"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, default=uuid4, nullable=False)
    user_id: Mapped[UUID] = mapped_column(uuid, ForeignKey("users.id"), unique=True, nullable=False)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    image: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationships """
    user = relationship("UserModel", back_populates="profile")



class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, nullable=False, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(uuid, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationships """
    user = relationship("UserModel", back_populates="tasks")