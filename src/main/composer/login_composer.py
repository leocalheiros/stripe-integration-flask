from src.infra.db.repositories.users_repository import UsersRepository
from src.controllers.login_controller import LoginController


def login_composer():
    repo = UsersRepository()
    controller = LoginController(repo)
    return controller
