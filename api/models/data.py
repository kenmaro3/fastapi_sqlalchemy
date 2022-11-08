from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

# from api.models.optimization import Optimization

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ref_x = Column(String(length=60))
    ref_y = Column(String(length=60))

    scalers = relationship("Scaler", back_populates="data")
    #model = relationship("Model", back_populates="data")
    
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="datas")

    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="datas")