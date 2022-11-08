from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

from api.models.data import Data


class Scaler(Base):
   __tablename__ = "scaler"
   id = Column(Integer, primary_key=True, autoincrement=True)
   preprocess_type = Column(String(length=30))

   # relation
   #users = relationship("User", secondary="user_scaler", back_populates="scalers")
   model = relationship("Model", back_populates="scaler")

   project_id = Column(Integer, ForeignKey("project.id"))
   project = relationship("Project", back_populates="scalers")

   data_id = Column(Integer, ForeignKey("data.id"))
   data = relationship("Data", back_populates="scalers")
