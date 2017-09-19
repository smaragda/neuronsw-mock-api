# coding: utf-8
from flask import json


class Project:
    def __init__(self, iid=-1, iname='N/A', izip_location='unknown zip location'):
        self.id = iid
        self.name = iname
        self.zip_location = izip_location

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @property
    def id(self) -> int:
        """
        Gets the id of this Project.

        :return: The id of this Project.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Project.

        :param id: The id of this Project.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Project.

        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Project.

        :param name: The name of this Project.
        :type name: str
        """

        self._name = name

    @property
    def zip_location(self) -> str:
        """
        Gets the zip_location of this Project.

        :return: The zip_location of this Project.
        :rtype: str
        """
        return self._zip_location

    @zip_location.setter
    def zip_location(self, zip_location: str):
        """
        Sets the zip_location of this Project.

        :param zip_location: The zip_location of this Project.
        :type zip_location: str
        """

        self._zip_location = zip_location
