from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flax import env

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = env.postgres_dsn

# Creating the SQLAlchemy ORM engine..>> above we have imported create_engine method
# from sqlalchemy
# Since we are using Postgres we dont need anything else

create_engine

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating SessionLocal class which will be database session on the request..

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
