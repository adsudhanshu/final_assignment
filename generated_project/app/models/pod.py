from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Pod(Base):
    __tablename__ = "pods"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    members = relationship("PodMember", backref="pod")