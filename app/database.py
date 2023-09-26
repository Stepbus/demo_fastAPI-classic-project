import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

load_dotenv()

SQLALCHEMY_DATABASE_URL = (f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@'
                           f'{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


################ psycopg2 ########################
# while True:
    # try:
    #     conn = psycopg2.connect(
    #         host=os.environ.get("POSTGRES_HOST"),
    #         port=5432,
    #         dbname=os.environ.get("POSTGRES_DB"),
    #         user=os.environ.get("POSTGRES_USER"),
    #         password=os.environ.get("POSTGRES_PASSWORD"),
    #         cursor_factory=RealDictCursor,
    #     )
    #     cursor = conn.cursor()
    #     print(f"Database connection was successful!")
    # except Exception as error:
    #     print(f"You got error: {error}")
################ psycopg2 ########################