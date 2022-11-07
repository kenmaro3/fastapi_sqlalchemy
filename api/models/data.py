from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

from api.models.preprocess_data import PreprocessData
from api.models.optimized_value import OptimizedValue

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ref = Column(String(length=30))
    
    ## foreign key
    #user_id = Column(Integer, ForeignKey("user.id"))
    #user = relationship("User", back_populates="datas")

    ## foreign key
    #project_id = Column(Integer, ForeignKey("project.id"))
    #project = relationship("Project", back_populates="datas")

    ## relation
    #preprocess_datas = relationship("PreprocessData", back_populates="data")
    ## relation
    #optimized_values = relationship("OptimizedValue", back_populates="data")