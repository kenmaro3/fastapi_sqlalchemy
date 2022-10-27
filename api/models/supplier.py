from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="suppliers")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="suppliers")