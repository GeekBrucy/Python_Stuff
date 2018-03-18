import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://brucy:brucy_getGoodJob@localhost/db_playground", encoding='utf-8', echo=True) # echo=True will print out detailed process

Base = declarative_base() # generate orm base class

class Product(Base):
  __tablename__ = 'products' # table name
  id = Column(Integer, primary_key = True)
  name = Column(String(32))
  price = Column(Integer)

  def __repr__(self):
    return "<Name: %s, Price: $%s>" %(self.name, self.price)

Base.metadata.create_all(engine) # create table schema


############## Create Data ##################
Session_class = sessionmaker(bind=engine) # create database dialog: session class, the return type of sessionmaker is class not instance
Session = Session_class() # generate session instance, similar as cursor in pymysql

# prod_obj = Product(name='MacBook Pro 2017 15-inch', price='2799') # generate data obj
# prod_obj2 = Product(name='MacBook Pro 2017 13-inch', price='1999') # generate data obj

# print(prod_obj.name, prod_obj.price)

# Session.add(prod_obj) 
# Session.add(prod_obj2)

# print(prod_obj.name, prod_obj.price)
# Session.commit() # if not commit, data won't go into database


############## Query Data ##################
# result = Session.query(Product).filter_by(name = "MacBook Pro 2017 15-inch").all()
# print(result[0].name, result[0].price)

# result = Session.query(Product).filter_by().all()
# print(result)

# result = Session.query(Product).filter(Product.name.like('%13-inch')).all()
# print(result)

# result = Session.query(Product).filter(Product.id > 1).all()
# print(result)

# result = Session.query(Product).filter(Product.id == 1).all()
# print(result)

# result = Session.query(Product).filter(Product.id == 1).first()
# result.name = "Dual Screen"
# result.price = 200
# Session.commit()



# fake_product = Product(name = 'Androios', price = 300)
# Session.add(fake_product)
# print(Session.query(Product).filter(Product.name == 'Androios').all())
# Session.rollback()
# print(Session.query(Product).filter(Product.name == 'Androios').all())


# print(Session.query(Product).count())


# from sqlalchemy import func
# print(Session.query(func.count(Product.name), Product.name).group_by(Product.name).all())

