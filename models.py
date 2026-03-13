from database import Base
from sqlalchemy import Column,Integer,Boolean,String

class todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    Task = Column(String(255))
    Description = Column(String(655))
    Priority = Column(Integer)
    Completed = Column(Boolean,default=False)