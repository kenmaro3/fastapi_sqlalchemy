from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from api.db import Base

class IntermediateUserProject(Base):
    __tablename__ = 'intermediate_user_project'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="intermediate_user_projects")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="intermediate_user_projects")