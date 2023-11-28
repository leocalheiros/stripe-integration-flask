from src.infra.db.repositories.users_repository import UsersRepository
from src.controllers.create_user_controller import CreatePerson


def create_user_composer():
    repo = UsersRepository()
    controller = CreatePerson(repo)
    return controller
