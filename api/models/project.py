from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

from api.models.user_project import UserProject
#from api.models.user import User
#from api.models.model import Model
#from api.models.preprocess_data import PreprocessData
#from api.models.optimized_value import OptimizedValue
#from api.schemas import user_project

class Project(Base):
   __tablename__ = "project"
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(length=30))

   # relation
   #users = relationship("User", secondary="user_project", back_populates="projects")
   users = relationship("UserProject", back_populates="project")
   ## relation
   #models = relationship("Model", back_populates="project")
   ## relation
   #preprocess_datas = relationship("PreprocessData", back_populates="project")
   ## relation
   #optimized_values = relationship("OptimizedValue", back_populates="project")
   ## relation
   #datas = relationship("Data", back_populates="project")
