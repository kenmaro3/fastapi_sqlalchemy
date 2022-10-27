from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class PreprocessData(Base):
    __tablename__ = "preprocess_data"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    model_id = Column(Integer, ForeignKey("model.id"))
    model = relationship("model", back_populates="preprocess_datas")

    # foreign key
    data_id = Column(Integer, ForeignKey("data.id"))
    data = relationship("data", back_populates="preprocess_datas")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("project", back_populates="preprocess_datas")

    preprocess_type = Column(String(30))