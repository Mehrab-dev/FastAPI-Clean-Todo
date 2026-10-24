from sqlalchemy import String, DateTime, Boolean, ForeignKey, Text, UUID as uuid
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from uuid import UUID, uuid4
from datetime import datetime

from app.infrastructure.database.base import Base
from app.shared.datetime import utc_now



class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, default=uuid4, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationship """
    profile = relationship("ProfileModel", back_populates="user", cascade="all, delete-orphan", uselist=False)
    tasks = relationship("TaskModel", back_populates="user", cascade="all, delete-orphan")



class ProfileModel(Base):
    __tablename__ = "profiles"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, default=uuid4, nullable=False)
    user_id: Mapped[UUID] = mapped_column(uuid, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    image: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationship """
    user = relationship("UserModel", back_populates="profile")



class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(uuid, primary_key=True, default=uuid4, nullable=False)
    user_id: Mapped[UUID] = mapped_column(uuid, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    """ relationship """
    user = relationship("UserModel", back_populates="tasks")