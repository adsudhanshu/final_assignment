from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Leave(Base):
    __tablename__ = "leaves"
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    leave_id = Column(Integer, ForeignKey("leaves.id"))
    status = Column(String, nullable=False, default="pending")
    employee = relationship("Employee", backref="leave_requests")
    leave = relationship("Leave", backref="leave_requests")