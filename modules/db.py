# pylint: disable=missing-docstring
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

import models
from sqlalchemy.orm import Session

def add_device