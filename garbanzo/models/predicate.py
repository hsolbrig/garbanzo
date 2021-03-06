# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Predicate(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, definition: str=None):
        """
        Predicate - a model defined in Swagger

        :param id: The id of this Predicate.
        :type id: str
        :param name: The name of this Predicate.
        :type name: str
        :param definition: The definition of this Predicate.
        :type definition: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'definition': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'definition': 'definition'
        }

        self._id = id
        self._name = name
        self._definition = definition

    @classmethod
    def from_dict(cls, dikt) -> 'Predicate':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Predicate of this Predicate.
        :rtype: Predicate
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Predicate.
        CURIE-encoded identifier of predicate resource 

        :return: The id of this Predicate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Predicate.
        CURIE-encoded identifier of predicate resource 

        :param id: The id of this Predicate.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Predicate.
        human readable name of predicate relation 

        :return: The name of this Predicate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Predicate.
        human readable name of predicate relation 

        :param name: The name of this Predicate.
        :type name: str
        """

        self._name = name

    @property
    def definition(self) -> str:
        """
        Gets the definition of this Predicate.
        human readable definition of predicate relation provided by this beacon 

        :return: The definition of this Predicate.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        """
        Sets the definition of this Predicate.
        human readable definition of predicate relation provided by this beacon 

        :param definition: The definition of this Predicate.
        :type definition: str
        """

        self._definition = definition

