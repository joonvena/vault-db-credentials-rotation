from sqlalchemy import create_engine
import psycopg2
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .utils import set_db_credentials


db_name = os.getenv("DB_NAME", "exampledb")
db_host = os.getenv("DB_HOST", "postgres")


def _get_new_connection():
    user, password = set_db_credentials()
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=db_host)
    return conn


engine = create_engine(
    'postgresql://',
    pool_recycle=300,
    creator=_get_new_connection,
    echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
