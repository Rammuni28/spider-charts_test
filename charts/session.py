from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from decouple import config
from urllib.parse import quote_plus

encoded_password = quote_plus(config('DB_PASSWORD'))
DATABASE_URL = f"mysql+pymysql://{config('DB_USER')}:{encoded_password}@{config('DB_HOST')}/{config('DB_NAME')}"
engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
