from sqlalchemy.exc import IntegrityError
from src.infra.db.settings.connection import db_connection_handler
from src.infra.db.entities.users import Users as UsersModel
from src.infra.db.repositories.interfaces.users_interface import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def create_user(cls, email: str, password: str) -> any:
        with db_connection_handler as database:
            user = UsersModel(email=email, password=password)
            database.session.add(user)
            try:
                database.session.commit()
                return user
            except IntegrityError as integrity_error:
                database.session.rollback()
                raise integrity_error
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_user_by_email(cls, email: str) -> any:
        with db_connection_handler as database:
            user = database.session.query(UsersModel).filter(UsersModel.email == email).first()
            return user

    @classmethod
    def delete_user_by_email(cls, email: str) -> any:
        with db_connection_handler as database:
            user = cls.get_user_by_email(email)
            if user:
                database.session.delete(user)
                database.session.commit()
                return user
            else:
                return None
