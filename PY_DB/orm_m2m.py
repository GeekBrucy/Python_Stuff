from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://brucy:brucy_getGoodJob@localhost/db_playground", encoding='utf-8')
Base = declarative_base()

custommer_m2m_product = Table('custommer_m2m_product', Base.metadata,
                      Column('customer_id',Integer,ForeignKey('customer.id')),
                      Column('product_id',Integer,ForeignKey('products.id')),
                      )
class Product(Base):
  __tablename__ = 'products' # table name
  id = Column(Integer, primary_key = True)
  name = Column(String(32))
  price = Column(Integer)
  customer = relationship('Customer', secondary=custommer_m2m_product,backref='products' )

  def __repr__(self):
    return self.name

class Customer(Base):
  __tablename__ = 'customer'
  id = Column(Integer, primary_key = True)
  name = Column(String(32))

  def __repr__(self):
    return self.name

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
s = Session_class()
# p1 = Product(name = "MBP 2017 15inch", price = 2799)
# p2 = Product(name = "MBP 2017 13inch", price = 1999)
# p3 = Product(name = "WASD Keyboard", price = 200)

# c1 = Customer(name = 'Brucy')
# c2 = Customer(name = 'Cindy')
# c3 = Customer(name = 'Bella')

# p1.customer = [c1, c2]
# p2.customer = [c2, c3]
# p3.customer = [c1, c2, c3]

# s.add_all([p1, p2, p3, c1, c2, c3])
# s.commit()

prod_obj = s.query(Product).first()
print(prod_obj.customer)
s.close()