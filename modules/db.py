# pylint: disable=missing-docstring, import-error
from models import Devices
from flask_restful import Resource, reqparse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create the engine
engine = create_engine('sqlite:///modules/database.db', echo=True)

# Initiate sessionmake to bind to the engine 
Session = sessionmaker(bind=engine)

# Resources for devices
class DeviceResouce(Resource):
    def get(self):
        '''Query device table'''
        session = Session()

        devices = session.query(Devices).all()
        session.close()
        return{'devices': [{'id':device.id, 'device':device.device, 
                            'name':device.name, 'desc':device.desc
                            } for device in devices]}, 200
    def post(self):
        # Parse the request data
        parser = reqparse.RequestParser()
        parser.add_argument('device', type=str, required=True)
        parser.add_argument('name', type=str, required=True)        
        parser.add_argument('desc', type=str, required=False)
        args = parser.parse_args()        

        # insert a device into the database
        with Session() as session:
            new_device = Devices(device=args['device'], name=args['name'], desc=args['desc'])
            session.add(new_device)
            session.commit()

        return {'message': 'Device added bitch!'}, 201