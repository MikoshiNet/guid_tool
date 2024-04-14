# pylint: disable=missing-docstring, import-error
# modules/db.py
from models import Devices
from flask_restful import Resource, reqparse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func

# Create the engine
engine = create_engine('sqlite:///modules/database.db', echo=True)

# Initiate sessionmake to bind to the engine 
Session = sessionmaker(bind=engine)

# Resources for devices
class DeviceInt(Resource):
    def get(self):
        '''Query device table'''
        session = Session()

        devices = session.query(Devices).all()
        session.close()
        return{'devices': [{'uid':device.uid, 'device':device.device, 
                            'desc':device.desc
                            } for device in devices]}, 200
    def post(self):
        # Parse the request data
        parser = reqparse.RequestParser()
        parser.add_argument('device', type=str, required=True)
        #parser.add_argument('name', type=str, required=True)        
        parser.add_argument('desc', type=str, required=False)
        args = parser.parse_args()

        # insert a device into the database
        with Session() as session:
            # Add 0's to the id
            next_id = session.query(func.max(Devices.id)).scalar() or 0
            uid = f'{str(next_id + 1).zfill(4)}{args["device"]}' # Combine id and device

            new_device = Devices(uid=uid, device=args['device'], desc=args['desc'])
            session.add(new_device)
            session.commit()

        return {'device_id': uid}, 201