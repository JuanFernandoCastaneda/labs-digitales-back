from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

motor = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
db = sessionmaker(autocommit=False, autoflush=False, bind=motor)()
ModeloBase = declarative_base()