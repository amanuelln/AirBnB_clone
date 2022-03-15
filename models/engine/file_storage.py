#!/usr/bin/python3
"""
This module contains code related to file storage
for the airbnb clone project. A json data format
for serialization and deserialization of data.
"""
import json
import models
from models.base_model import BaseModel
from os import path

class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """
        Public instance method to return
        the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Public instance method that
        sets in __objects with key id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Public instance that serializes __objects
        to the JSON file
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        Public instance method to deserialize the JSON file
        to __objects only if file exists
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
