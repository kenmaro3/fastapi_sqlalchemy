from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

from api.models.intermediate_user_project import IntermediateUserProject
from api.models.model import Model
from api.models.preprocess_data import PreprocessData
from api.models.optimized_value import OptimizedValue
from api.schemas import intermediate_user_project

class Project(Base):
   __tablename__ = "project"
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(length=30))

   # relation
   intermediate_user_projects = relationship("IntermediateUserProject", back_populates="project")
   # relation
   models = relationship("Model", back_populates="project")
   # relation
   preprocess_datas = relationship("PreprocessData", back_populates="project")
   # relation
   optimized_values = relationship("OptimizedValue", back_populates="project")
   # relation
   datas = relationship("Data", back_populates="project")
