#!/usr/bin/python3
""" State Module for HBNB project """

import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(
        String(128), nullable=False
    ) if os.getenv("HBNB_TYPE_STORAGE") == "db" else ""

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete-orphan", backref="state")

    else:
        @property
        def cities(self):
            """
            Returns list of City instances with state_id equals
            to State.id
            """
            from models import storage

            cities_states  = []

            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_states.append(city)

            return cities_states
