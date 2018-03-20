from sqlalchemy import Column, String, Integer, create_engine, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key = True)
  name = Column(String(20))
  birthday = Column(Date)

# class Book(Base):
#   __tablename__ = 'book'
#   id = Column(Integer, primary_key = True)
#   name = Column(String(30))
#   category = Column(String(20))

engine = create_engine('mysql+pymysql://brucy:brucy_getGoodJob@localhost/db_playground', encoding='utf-8')
# engine = create_engine("mysql+pymysql://brucy:brucy_getGoodJob@localhost/db_playground", encoding='utf-8')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)
# new_user = User(name = "Brucy", birthday = datetime.date(1988, 10, 6))
# session.add(new_user)

# session.commit()
session.close()