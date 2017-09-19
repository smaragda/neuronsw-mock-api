# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.inline_response2001_labels import InlineResponse2001Labels
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class LabelsCollection(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, labels: List[InlineResponse2001Labels]=None):
        """
        LabelsCollection - a model defined in Swagger

        :param labels: The labels of this LabelsCollection.
        :type labels: List[InlineResponse2001Labels]
        """
        self.swagger_types = {
            'labels': List[InlineResponse2001Labels]
        }

        self.attribute_map = {
            'labels': 'labels'
        }

        self._labels = labels

    @classmethod
    def from_dict(cls, dikt) -> 'LabelsCollection':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LabelsCollection of this LabelsCollection.
        :rtype: LabelsCollection
        """
        return deserialize_model(dikt, cls)

    @property
    def labels(self) -> List[InlineResponse2001Labels]:
        """
        Gets the labels of this LabelsCollection.

        :return: The labels of this LabelsCollection.
        :rtype: List[InlineResponse2001Labels]
        """
        return self._labels

    @labels.setter
    def labels(self, labels: List[InlineResponse2001Labels]):
        """
        Sets the labels of this LabelsCollection.

        :param labels: The labels of this LabelsCollection.
        :type labels: List[InlineResponse2001Labels]
        """

        self._labels = labels

