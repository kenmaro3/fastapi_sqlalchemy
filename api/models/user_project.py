from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class UserProject(Base):
    __tablename__ = 'user_project'
    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)