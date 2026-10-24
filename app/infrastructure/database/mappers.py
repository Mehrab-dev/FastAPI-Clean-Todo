
from app.infrastructure.database import models
from app.domain.entities import entities


class UserMapper:
    @staticmethod
    def to_model(entity: entities.User) -> models.UserModel:
        return models.UserModel(
            id=entity.id,
            email=entity.email,
            password=entity.password,
            is_active=entity.is_active,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    @staticmethod
    def to_update(entity: entities.User, model: models.UserModel) -> None:
        model.email = entity.email
        model.password = entity.password
        model.is_active = entity.is_active
        model.updated_at = entity.updated_at

    @staticmethod
    def to_domain(model: models.UserModel) -> entities.User:
        return entities.User(
            id=model.id,
            email=model.email,
            password=model.password,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at
        )



class ProfileMapper:
    @staticmethod
    def to_model(entity: entities.Profile) -> models.ProfileModel:
        return models.ProfileModel(
            id=entity.id,
            user_id=entity.user_id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            bio=entity.bio,
            image=entity.image,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    @staticmethod
    def to_update(entity: entities.Profile, model: models.ProfileModel) -> None:
        model.first_name = entity.first_name
        model.last_name = entity.last_name
        model.bio = entity.bio
        model.image = entity.image
        model.updated_at = entity.updated_at

    @staticmethod
    def to_domain(model: models.ProfileModel) -> entities.Profile:
        return entities.Profile(
            id=model.id,user_id=model.user_id,
            first_name=model.first_name,
            last_name=model.last_name,
            bio=model.bio,
            image=model.image,
            created_at=model.created_at,
            updated_at=model.updated_at
        )


class TaskMapper:
    @staticmethod
    def to_model(entity: entities.Task) -> models.TaskModel:
        return models.TaskModel(
            id=entity.id,
            user_id=entity.user_id,
            title=entity.title,
            description=entity.description,
            is_done=entity.is_done,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    @staticmethod
    def to_update(entity: entities.Task, model: models.TaskModel) -> None:
        model.title = entity.title
        model.description = entity.description
        model.is_done = entity.is_done
        model.updated_at = entity.updated_at

    @staticmethod
    def to_domain(model: models.TaskModel) -> entities.Task:
        return entities.Task(
            id=model.id,
            user_id=model.user_id,
            title=model.title,
            description=model.description,
            is_done=model.is_done,
            created_at=model.created_at,
            updated_at=model.updated_at
        )