from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class Buyer(Base):
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="buyers")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="buyers")