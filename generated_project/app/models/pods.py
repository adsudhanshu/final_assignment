from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pod(Base):
    __tablename__ = "pods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    members = relationship("PodMember", backref="pod")

class PodMember(Base):
    __tablename__ = "pod_members"
    id = Column(Integer, primary_key=True)
    pod_id = Column(Integer, ForeignKey("pods.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    role = Column(String, nullable=False)
    pod = relationship("Pod", backref="pod_members")
    employee = relationship("Employee", backref="pod_members")