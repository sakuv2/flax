from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@10.8.1.4/flax"

# Creating the SQLAlchemy ORM engine..>> above we have imported create_engine method
# from sqlalchemy
# Since we are using Postgres we dont need anything else

create_engine

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating SessionLocal class which will be database session on the request..

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating the base clase, using the declerative_base() method which returns a class.
# Later we will need this Base Class to create each of the database models

Base = declarative_base()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
