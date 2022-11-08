from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, autoincrement=True)

    ## relation
    #preprocess_datas = relationship("PreprocessData", back_populates="model")
    ## relation
    #optimized_values = relationship("OptimizedValue", back_populates="model")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="models")

    scaler_id = Column(Integer, ForeignKey("scaler.id"))
    scaler = relationship("Scaler", back_populates="model", uselist=False)

    # data_id = Column(Integer, ForeignKey("data.id"))
    # data = relationship("Data", back_populates="model", uselist=False)

    optimization_id = Column(Integer, ForeignKey("optimization.id"))
    optimization = relationship("Optimization", back_populates="models")


    ref = Column(String(length=30))
    status = Column(String(length=30))
    estimated_time = Column(Integer)
    train_start_ts = Column(String(30))
    train_finish_ts = Column(String(30))
    parameters = Column(String(length=30))