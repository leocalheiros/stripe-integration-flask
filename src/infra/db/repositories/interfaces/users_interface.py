from abc import ABC, abstractmethod


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str) -> any:
        pass

    def get_user_by_email(self, email: str) -> any:
        pass

    def delete_user_by_email(self, email: str) -> any:
        pass
