#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """Returns a list of City instances with state_id
        equal to the current State.id."""
        cities = models.storage.all(City)
        city_instances = []
        for city in cities.values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
