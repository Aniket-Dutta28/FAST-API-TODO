from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql + pymysql://root:aniket28@localhost/todo_project"

Engine = create_engine(DATABASE_URL)
session_local = sessionmaker(bind=Engine,autoflush=False)
Base = declarative_base()