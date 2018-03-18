import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://brucy:brucy_getGoodJob@localhost/db_playground", encoding='utf-8') # echo=True will print out detailed process

Base = declarative_base() # generate orm base class

class Students(Base):
  __tablename__ = 'student'
  id = Column(Integer, primary_key = True)
  name = Column(String(32), nullable = False)
  register_date = Column(Date, nullable = False)

  def __repr__(self):
    return "<%s name: %s>" % (self.id, self.name)


class StudyRecord(Base):
  __tablename__ = 'study_record'
  id = Column(Integer, primary_key = True)
  day = Column(Integer, nullable = False)
  status = Column(String(32))
  stu_id = Column(Integer, ForeignKey('student.id'))

  student = relationship("Students", backref = "my_classes")
  def __repr__(self):
    return "<%s Day: %s Status: %s>" % (self.student.name, self.day, self.status)

Base.metadata.create_all(engine)

###################### Insert Data #####################
Session_class = sessionmaker(bind=engine) # create database dialog: session class, the return type of sessionmaker is class not instance

Session = Session_class() # generate session instance, similar as cursor in pymysql

# s1 = Students(name = "Brucy", register_date = '2017-05-26')
# s2 = Students(name = "Bella", register_date = '2017-04-26')
# s3 = Students(name = "Bacon", register_date = '2017-12-26')
# s4 = Students(name = "Cheese", register_date = '2017-02-26')

# study_obj1 = StudyRecord(day = 1, status = 'Yes', stu_id = 1)
# study_obj2 = StudyRecord(day = 2, status = 'No', stu_id = 1)
# study_obj3 = StudyRecord(day = 3, status = 'Yes', stu_id = 1)
# Session.add_all([s1, s2, s3, s4, study_obj1, study_obj2, study_obj3])

stu_obj = Session.query(Students).filter(Students.name == 'Brucy').first()
print(stu_obj.my_classes)

# Session.commit()