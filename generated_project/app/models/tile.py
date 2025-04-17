from sqlalchemy import Column, Integer, String
from database import Base

class Tile(Base):
    __tablename__ = "tiles"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_role = Column(String)