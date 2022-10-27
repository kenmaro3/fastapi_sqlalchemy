from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base
from api.models.supplier import Supplier


class OptimizedValue(Base):
    __tablename__ = "optimized_value"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    model_id = Column(Integer, ForeignKey("model.id"))
    model = relationship("model", back_populates="optimized_values")

    # foreign key
    data_id = Column(Integer, ForeignKey("data.id"))
    data = relationship("data", back_populates="optimized_values")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("project", back_populates="optimized_values")