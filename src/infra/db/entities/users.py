from sqlalchemy import Column, String, Integer, BIGINT
from src.infra.db.settings.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
