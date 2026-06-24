"""Model class for  tbl_informacion"""
from sqlalchemy import Column,Integer,String,Boolean,SMALLINT,ForeignKey
from config.database import Base

class UsersInformationModel(Base):
    """Users informacion class"""
    __tablename__ = "tbl_personal_information"

    id_informacion = Column(SMALLINT,primary_key=True,autoincrement=True)
    id_user = Column(Integer,
                        ForeignKey("tbl_users.id_user",ondelete="CASCADE"),nullable=False
                        )
    first_name = Column(String(50))
    paternal_surname = Column(String(50))
    maternal_surname = Column(String(50))
    cell_phone = Column(String(12))
    last = Column(Boolean,default=True)

