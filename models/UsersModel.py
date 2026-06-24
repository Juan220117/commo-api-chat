"""Model class for tbl_users"""
from sqlalchemy import Column,String,SMALLINT
from config.database import (Base)

class UsersModel(Base):
    """User mapping class"""
    __tablename__ = "tbl_users"

    id_user = Column(SMALLINT,primary_key=True,autoincrement=True)
    username = Column(String(50))
    password = Column(String(100))
    email = Column(String(100))

