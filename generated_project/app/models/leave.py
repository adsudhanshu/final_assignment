from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    reason = Column(String)
    status = Column(String)

    leave_requests = relationship("LeaveRequest", backref="leave")