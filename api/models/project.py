from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

from api.models.supplier import Supplier
from api.models.buyer import Buyer
from api.models.model import Model
from api.models.preprocess_data import PreprocessData
from api.models.optimized_value import OptimizedValue

class Project(Base):
   __tablename__ = "project"
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(length=30))

   # relation
   suppliers = relationship("Supplier", back_populates="project")
   # relation
   buyers = relationship("Buyer", back_populates="project")
   # relation
   models = relationship("Model", back_populates="project")
   # relation
   preprocess_datas = relationship("PreprocessData", back_populates="project")
   # relation
   optimized_values = relationship("OptimizedValue", back_populates="project")
   # relation
   datas = relationship("Data", back_populates="project")
