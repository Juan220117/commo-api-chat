"""Class for queries to the tbl_users table"""
from sqlalchemy.orm import Session
from typing import Optional, List
from models.UsersModel import UsersModel

class UsersRepository(object):
    """Query class """
    def __init__(self, session: Session):
        self.session = session

    def create_user(self,new_user:UsersModel) -> None:
        """Query to generate a new user"""
        self.session.add(new_user)
        self.session.flush()

    def get_user_by_username(self,username:str) -> UsersModel:
        """Query to get the record by username"""
        return (
            self.session.query(UsersModel)
            .filter(UsersModel.username == username)
            .first()
        )

    def get_user_by_user_name_or_email(self,username:str,email:str) -> None | str:
        """Query to check if a user or password already exists """
        response = None
        record_username = (
            self.session.query(UsersModel)
            .filter(UsersModel.username == username).
            first()
        )
        
        record_email = (
            self.session.query(UsersModel)
            .filter(UsersModel.email == email)
            .first()
        )
        if record_username:
            response = f"The user:{username} already registered"
        elif record_email:
            response = f"The mail:{email} already registered"

        return response
