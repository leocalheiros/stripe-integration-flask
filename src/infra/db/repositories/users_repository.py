from sqlalchemy.exc import IntegrityError, NoResultFound
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
            try:
                result = database.session.query(UsersModel.id, UsersModel.email, UsersModel.password).filter(
                    UsersModel.email == email).one()
                user_data = {
                    'id': result[0],
                    'email': result[1],
                    'password': result[2],
                }
                return user_data
            except NoResultFound:
                return None
            except Exception as exception:
                database.session.rollback()
                raise exception

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
