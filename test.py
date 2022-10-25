import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# declaration
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    password = Column(String(30))

    # relation: relates to user property in Supplier Class
    suppliers = relationship("Supplier", back_populates="user")

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # foreign key
    user_id = Column(Integer, ForeignKey("user.id"))
    # needs to have relation with User class suppliers property
    user = relationship("User", back_populates="suppliers")

    # foreign key
    project_id = Column(Integer, ForeignKey("project.id"))
    # needs to have relation with User class suppliers property
    project = relationship("Project", back_populates="suppliers")

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))

    suppliers = relationship("Supplier", back_populates="project")



def mock_initial(engine):
    # drop table
    Base.metadata.drop_all(engine)
    # create table
    Base.metadata.create_all(engine)


def mock_get_session(engine):
    # prepare session to connect
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    return session


def mock_prepare(session):

    # create user
    user1 = User(name='user1', password="password1")
    session.add(user1)
    session.commit()

    #create project
    project1 = Project(name="project1")
    session.add(project1)
    project2 = Project(name="project2")
    session.add(project2)
    session.commit()


    print("\nafter add==============")
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name, user.password)

    # create supplier and add supplier.user_id as user.id
    # also relates project as supplier.project_id
    user = session.query(User).filter_by(id=1).one()
    supplier = Supplier()
    supplier.user_id = user.id

    project = session.query(Project).filter_by(id=1).one()
    supplier.project_id = project.id
    session.add(supplier)
    session.commit()

    # create supplier and add supplier.user_id as user.id
    # also relates project as supplier.project_id
    user = session.query(User).filter_by(id=1).one()
    supplier = Supplier()
    supplier.user_id = user.id

    project = session.query(Project).filter_by(id=2).one()
    supplier.project_id = project.id
    session.add(supplier)
    session.commit()


def get_projects(session, user_id: int):
    print("\nafter add supplier==============")
    user = session.query(User).filter_by(id=user_id).one()

    projects_id = []
    for el in user.suppliers:
        projects_id.append(el.project_id)

    projects = session.query(Project).filter(Project.id.in_(projects_id)).all()
    return projects
    #for el in projects:
    #    print(el.id, el.name)



if __name__ == "__main__":
    print("hello, world")
    # connection to db
    engine = sqlalchemy.create_engine('sqlite:///sample_db.sqlite3', echo=True)


    mock_initial(engine)
    session = mock_get_session(engine)
    mock_prepare(session)
    print("\n\n==================")
    projects = get_projects(session, 1)

    quit()

    #users = session.query(User).filter_by(name='user1').all()
    #for user in users:
    #    session.delete(user)
    #session.commit()

    #print("\nafter delete============")
    #users = session.query(User).all()
    #for user in users:
    #    print(user.id, user.name, user.password)


