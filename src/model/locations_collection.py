# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class LocationsCollection(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, devices: List[str]=None, locations: List[str]=None, places: List[str]=None):
        """
        LocationsCollection - a model defined in Swagger

        :param devices: The devices of this LocationsCollection.
        :type devices: List[str]
        :param locations: The locations of this LocationsCollection.
        :type locations: List[str]
        :param places: The places of this LocationsCollection.
        :type places: List[str]
        """
        self.swagger_types = {
            'devices': List[str],
            'locations': List[str],
            'places': List[str]
        }

        self.attribute_map = {
            'devices': 'devices',
            'locations': 'locations',
            'places': 'places'
        }

        self._devices = devices
        self._locations = locations
        self._places = places

    @classmethod
    def from_dict(cls, dikt) -> 'LocationsCollection':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocationsCollection of this LocationsCollection.
        :rtype: LocationsCollection
        """
        return deserialize_model(dikt, cls)

    @property
    def devices(self) -> List[str]:
        """
        Gets the devices of this LocationsCollection.

        :return: The devices of this LocationsCollection.
        :rtype: List[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices: List[str]):
        """
        Sets the devices of this LocationsCollection.

        :param devices: The devices of this LocationsCollection.
        :type devices: List[str]
        """

        self._devices = devices

    @property
    def locations(self) -> List[str]:
        """
        Gets the locations of this LocationsCollection.

        :return: The locations of this LocationsCollection.
        :rtype: List[str]
        """
        return self._locations

    @locations.setter
    def locations(self, locations: List[str]):
        """
        Sets the locations of this LocationsCollection.

        :param locations: The locations of this LocationsCollection.
        :type locations: List[str]
        """

        self._locations = locations

    @property
    def places(self) -> List[str]:
        """
        Gets the places of this LocationsCollection.

        :return: The places of this LocationsCollection.
        :rtype: List[str]
        """
        return self._places

    @places.setter
    def places(self, places: List[str]):
        """
        Sets the places of this LocationsCollection.

        :param places: The places of this LocationsCollection.
        :type places: List[str]
        """

        self._places = places
