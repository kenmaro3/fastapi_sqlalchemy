from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

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
