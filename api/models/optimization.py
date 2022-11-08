from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base


class Optimization(Base):
    __tablename__ = "optimization"
    id = Column(Integer, primary_key=True, autoincrement=True)
    parameters = Column(String(length=60))
    optimized_xs_ref = Column(String(length=60))

    models = relationship("Model", back_populates="optimization")

    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="optimizations")

    ## foreign key
    #model_id = Column(Integer, ForeignKey("model.id"))
    #model = relationship("Model", back_populates="optimized_values")

    ## foreign key
    #data_id = Column(Integer, ForeignKey("data.id"))
    #data = relationship("Data", back_populates="optimized_values")

    ## foreign key
    #project_id = Column(Integer, ForeignKey("project.id"))
    #project = relationship("Project", back_populates="optimized_values")