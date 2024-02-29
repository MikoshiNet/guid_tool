# pylint: disable=missing-docstring
import json
import os

def get_file_json_content(file_path, encoding = 'utf-8') -> dict:
    """
    Returns the JSON files' entire content as a dictionary or None if the file doesn't exist
    """
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r', encoding=encoding) as file:
        json_content = json.load(file)

    return json_content

def set_file_json_content(file_path: str, data: list, encoding='utf-8'):
    """
    This sets a files content to the data, formatted in json
    """
    dir_name = os.path.dirname(file_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=4)
