#!/usr/bin/python3
"""
Module contains BaseModel class
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel that defines all
    common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at = datetime.today()
        fmt = "%Y-%m-%dT%H:%M:S.%f"
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    self.__dict__[k] = datetime.strptime(v, fmt)
                else:
                    self.__dict__[k] = v
            models.storage.new(self)

    def __str__(self):
        """
        prints str format of class instance
        """
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__ ))

    def save(self):
        """
        updates update_at - time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns BaseModel dictionary instance"""
        Bdict = self.__dict__.copy()
        Bdict["created_at"] = self.created_at.isoformat()
        Bdict["updated_at"] = self.updated_at.isoformat()
        Bdict["__class__"] = self.__class__.__name__
        return Bdict
