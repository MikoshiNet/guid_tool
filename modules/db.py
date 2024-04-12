# pylint: disable=missing-docstring, import-error
'''Pevious code (Using as guidlines)'''
###from modules.file_handler import get_file_json_content, set_file_json_content
###
###class Database:
###    def __init__(self, path):
###        self.path = path
###        self._get()
###
###    def _get(self):
###        self.database = get_file_json_content(self.path)
###
###    def _set(self):
###        set_file_json_content(self.path, self.database)
###
###    def post_id(self, device_type, description):
###        new_id = self.database['devices'][len(self.database['devices'])][1] + 1
###        self.database['devices'].append(device_type, new_id, description, "")
###
###        return f"{device_type}{new_id}"

# modules/db.py
# Antglo 3/4/2024
### This will have examples on how to manipulate items within the DB using the Session

from models import engine, Devices
<<<<<<< HEAD
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)
# create a session
session = Session()

# Add a device to the database [ device, name, desc ]
def add_device():
=======
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Session = sessionmaker

Session.configure(bind=engine)

#add a device to the database [ device, name, desc ]
def add_device(device_name, device_desc):
>>>>>>> 395fa0f (patch)
    '''This is an example on how it is done'''
    with Session() as session:
        sca = Devices(
            device='sca',
            name='Security Appliance',
            desc='This is a security appliance'
        )
    
        session.add(sca)
        session.commit()

<<<<<<< HEAD
add_device()

# Using select statement to query database.db
stmt = session.query(Devices).filter(Devices.id == "1").all() # .one() can be used for a specific query
print(stmt)
=======
def query_device():
    '''Query device table'''
    session = Session()

    devices = session.query(Devices).all()

    session.close()

    return devices

if __name__ == '__main__':
    add_device('exmaple', 'example desc for the example')

    devices = query_device()
    print('Example: ')
    for device in devices:
        print(device)
>>>>>>> 395fa0f (patch)
