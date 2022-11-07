from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base
from api.models.user_project import UserProject
from api.models.project import Project
#from api.models.data import Data

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=30))
    password = Column(String(length=30))

    # relation
    #projects = relationship("Project", secondary="user_project", back_populates="users")
    projects = relationship("UserProject", back_populates="user")
    ## relation
    #datas = relationship("Data", back_populates="user")
