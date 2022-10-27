from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base
from api.models.preprocess_data import PreprocessData
from api.models.optimized_value import OptimizedValue

class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # relation
    preprocess_datas = relationship("PreprocessData", back_populates="model")
    # relation
    optimized_values = relationship("OptimizedValue", back_populates="model")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="models")

    ref = Column(String(length=30))
    status = Column(String(length=30))
    estimated_time = Column(Integer)
    train_start_ts = Column(DateTime)
    train_finish_ts = Column(DateTime)
    parameters = Column(String(length=30))