"""Class for querues to the tbl_personal_information"""
from sqlalchemy.orm import Session
from typing import Any
from models.UsersInfoModel import UsersInformationModel

class UserInformationRepository(object):
    """Query class """
    def __init__(self,session:Session) -> None:
        self.session = session

    def save_personal_information(self,data:UsersInformationModel) -> None:
        """Query to save personal information"""
        self.session.add(data)
        self.session.flush()

