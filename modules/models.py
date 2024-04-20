# pylint: disable=missing-docstring
# modules/models.py Antglo 3/4/2024
### This file contains the metadata necessary to create tables and declarative bases/mappings

# import necessary constructs
from sqlalchemy import String, create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Declare the engine to connect to your DB
engine = create_engine('sqlite:///modules/database.db', echo=True) # echo flag instructs the engine to log all the SQL it emits to a python logger 

# DeclarativeBase by making a subclasses of Base
Base = declarative_base()

# Define the class for the table (Devices)
class Devices(Base):
    __tablename__ = 'devices'
    
    id = Column(Integer, primary_key=True) # the mapped_column allows you to further customize the column
    uid = Column(String(15))
    device = Column(String(15))
    desc = Column(String)
    
    # add an __init__ constructor to allow them as arguments
    def __init__(self, uid, device, desc):
        #self.id = id
        self.uid = uid
        self.device = device
        self.desc = desc
    
    # The method __repr__ is not necessary used for debugging
    def __repr__(self) -> str:
        return f'Devices(id={self.id!r}, device={self.device!r}, desc={self.desc!r})'

# start the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)