from database import Base
from sqlalchemy import Column,Integer,Boolean,String,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class todo(Base):
    __tablename__ = "todos_table"
    id = Column(Integer,primary_key=True,index=True)
    Task = Column(String(255))
    Description = Column(String(655))
    Priority = Column(Integer)
    Completed = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    owner = relationship("User", back_populates="todos")



class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    todos = relationship("Todo", back_populates="owner")
