#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ("created_at", "updated_at") and isinstance(v, str):
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)

            if not hasattr(kwargs, "id"):
                self.id = str(uuid.uuid4())
            if not hasattr(kwargs, "created_at"):
                self.created_at = datetime.utcnow()
            if not hasattr(kwargs, "updated_at"):
                self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f"[{cls}] ({self.id}) {self.__dict__}"
    
    def delete(self):
        """ delete the current instance from the storage"""
        from models import storage

        storage.delete(self)
    
    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        
        for key, value in self.__dict__.items():
            if key != "_sa_instance_state":
                if isinstance(value, datetime):
                    dictionary[key] = value.isoformat()
                else:
                    dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__

        return dictionary
