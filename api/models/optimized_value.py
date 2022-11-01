from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base


class OptimizedValue(Base):
    __tablename__ = "optimized_value"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    model_id = Column(Integer, ForeignKey("model.id"))
    model = relationship("Model", back_populates="optimized_values")

    # foreign key
    data_id = Column(Integer, ForeignKey("data.id"))
    data = relationship("Data", back_populates="optimized_values")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="optimized_values")