# pylint: disable=missing-docstring
# modules/models.py Antglo 3/4/2024
### This file contains the metadata necessary to create tables and declarative bases/mappings

# import necessary constructs
from typing import Any, List
from typing import Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Declare the engine to connect to your DB
engine = create_engine('sqlite:///:memory:', echo=True) # echo flag instructs the engine to log all the SQL it emits to a python logger 

# DeclarativeBase by making a subclasses of Base
class Base(DeclarativeBase):
    def __init__(self, id):
        self.id = id

# Define the class for the table (Devices)
class Devices(Base):
    __tablename__ = 'devices'
    
    id: Mapped[int] = mapped_column(primary_key=True) # the mapped_column allows you to further customize the column
    device: Mapped[str] = mapped_column(String(15))
    name: Mapped[str] = mapped_column(String(15))
    desc: Mapped[Optional[str]]
    
    # The method __repr__ is not necessary used for debugging
    def __repr__(self) -> str:
        return f'Devices(id={self.id!r}, device={self.device!r}, name={self.name!r}, desc={self.desc!r})'

# start the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)