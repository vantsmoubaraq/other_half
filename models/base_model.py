#!/usr/bin/env python3

"""
This modules implements the parent class, BaseModel
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This class implements the parent class, BaseModel
    """
    def __init__(self,*args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if (len(kwargs)):
            for key, value in kwargs.items():
                if (key == "created_at"):
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif (key == "updated_at"):
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if (key != "__class__"):
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = dict(self.__dict__)
        obj_dict["created_at"] = self.created_at.isoformat(sep="T")
        obj_dict["updated_at"] = self.updated_at.isoformat(sep="T")
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
