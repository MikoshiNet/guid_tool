# pylint: disable=missing-docstring
# antglo modules/api.py
# april 11, 2024

from flask import Flask
from flask_restful import Api
from db import DeviceResouce

# Create Flask app
app = Flask(__name__)
api = Api(app)

# Add resource to API
api.add_resource(DeviceResouce, '/devices')

if __name__ == '__main__':
    app.run(debug=True)