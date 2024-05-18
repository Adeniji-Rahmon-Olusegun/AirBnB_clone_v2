#!/usr/bin/python3
"""Module conatins database setup for airbnb clone project"""


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """SQL Alchemy database setup"""

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        data_base = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        db_url = f"mysql+mysqldb://{user}:{passwd}@{host}:3306/{data_base}"

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary: (like FileStorage)"""
        objs = dict()

        #classes = (User, State, City, Amenity, Place, Review)
        classes = (State, City, User)

        if cls is None:
            for class_ in classes:
                query = self.__session.query(class_)
                for obj in query.all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objs[key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                objs[key] = obj

        return objs

    def new(self, obj):
        """Adds the object to the current database session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.query(type(obj)).filter(type(obj).id == obj.id).delete(
                    synchronize_session=False)

    def reload(self):
        """Creates all tables in the database"""

        Base.metadata.create_all(self.__engine)

        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()
