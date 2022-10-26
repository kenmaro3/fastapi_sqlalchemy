from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

# declaration
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(String)

    # relation
    suppliers = relationship("Supplier", back_populates="user")
    # relation
    buyers = relationship("Buyer", back_populates="user")


class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="suppliers")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="suppliers")

class Buyer(Base):
    __tablename__ = 'buyer'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="buyers")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="buyers")


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    # relation
    suppliers = relationship("Supplier", back_populates="project")
    # relation
    buyers = relationship("Buyer", back_populates="project")
    # relation
    models = relationship("Model", back_populates="project")
    # relation
    preprocess_datas = relationship("PreprocessData", back_populates="project")
    # relation
    optimized_values = relationship("OptimizedValue", back_populates="project")


class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="models")

    ref = Column(String)
    status = Column(String)
    estimated_time = Column(Integer)
    train_start_ts = Column(DateTime)
    train_finish_ts = Column(DateTime)
    parameters = Column(String)


class PreprocessData(Base):
    __tablename__ = "preprocess_data"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    model_id = Column(Integer, ForeignKey("model.id"))
    model = relationship("model", back_populates="preprocess_datas")

    # foreign key
    data_id = Column(Integer, ForeignKey("data.id"))
    data = relationship("data", back_populates="preprocess_datas")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("project", back_populates="preprocess_datas")

    preprocess_type = Column(String)

    
class OptimizedValue(Base):
    __tablename__ = "optimized_value"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    model_id = Column(Integer, ForeignKey("model.id"))
    model = relationship("model", back_populates="optimized_values")

    # foreign key
    data_id = Column(Integer, ForeignKey("data.id"))
    data = relationship("data", back_populates="optimized_values")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("project", back_populates="optimized_values")


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ref = Column(String)
    
    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("user", back_populates="datas")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("project", back_populates="datas")

    # relation
    preprocess_datas = relationship("PreprocessData", back_populates="data")
    # relation
    optimized_values = relationship("OptimizedValue", back_populates="data")


