from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite_//pizzaria.db') # Base de dados SQLite
Base = declarative_base() # Classe base para os modelos

class User(Base):
    __tablename__ = 'users' # Nome da tabela
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    name = Column("name",String)
    email = Column("email",String,nullable=False) # Preenchimento obrigatorio
    password = Column("password",String)
    active = Column("active",Boolean)
    admin = Column("admin",Boolean,default=False)

    def __init__(self,name,email,password,active=True,admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class Order(Base):
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    user = Column("user",ForeignKey("user.id"),nullable=False)
    status = Column("status",String,nullable=False) # Preenchimento obrigatorio
    price = Column("price",float)
    # items = 

    def __init__(self,user,status="pending",price=0):
        self.user = user
        self.status = status
        self.price = price

class OrderItems(Base):
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    quantity = Column("quantity",Integer("user.id"),nullable=False)
    flavour = Column("flavour",String) # Preenchimento obrigatorio
    size = Column("size",float)
    unit_price = Column("unit_price", Float)
    order = Column("order", ForeignKey("order.id"))

    def __init__(self,quantity,flavour,size,unit_price,order):
        self.quantity = quantity
        self.flavour = flavour
        self.size = size
        self.unit_price = unit_price
        self.order = order
    
