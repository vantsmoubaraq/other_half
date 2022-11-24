#!/usr/bin/python3

"""
Module serializes instances to a JSON file and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json
from os import path
from os import read

class FileStorage:
    """
    class serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = key.split(".")[0]
                new_object = eval(class_name)(**value)
                self.new(new_object)
        except FileNotFoundError:
            pass

