import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,JSON,DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

load_dotenv()
Base =declarative_base()
class PersistentGraphState(Base):
    __tablename__ = "graph_state"

    id= Column(String, primary_key=True)
    timestamp=Column(DateTime,default = datetime.datetime.utcnow)
    srs_hash=Column(String)
    components =Column(JSON)


DATABASE_URL= os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)



Base.metadata.create_all(engine)

print("Database initialized!")