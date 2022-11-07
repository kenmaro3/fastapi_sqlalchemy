from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from api.db import Base

class UserProject(Base):
    __tablename__ = 'user_project'
    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)

    role = Column(String(30), nullable=False)

    user = relationship("User", back_populates="projects")
    project = relationship("Project", back_populates="users")

    # proxies
    user_name = association_proxy(target_collection="user", attr="name")
    project_name = association_proxy(target_collection="project", attr="name")