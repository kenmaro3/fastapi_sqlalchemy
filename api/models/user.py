from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base
from api.models.supplier import Supplier
from api.models.buyer import Buyer
from api.models.project import Project

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=30))
    password = Column(String(length=30))

    # relation
    suppliers = relationship("Supplier", back_populates="user")
    # relation
    buyers = relationship("Buyer", back_populates="user")
