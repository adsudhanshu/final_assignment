from sqlalchemy import Column, Integer, String
from app.database import Base

class Tile(Base):
    __tablename__ = "tiles"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_role = Column(String, nullable=False)