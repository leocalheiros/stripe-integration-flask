from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.database_configs import database_infos


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = database_infos["DATABASE_URL"]
        self.engine = create_engine(self.__connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()


db_connection_handler = DBConnectionHandler()
