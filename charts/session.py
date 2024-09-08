from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from decouple import config

DATABASE_URL = f"mysql+pymysql://{config('DB_USER')}:{config('DB_PASSWORD').replace('@', '%40')}@{config('DB_HOST')}/{config('DB_NAME')}"
engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
