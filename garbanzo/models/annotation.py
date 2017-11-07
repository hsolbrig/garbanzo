# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Annotation(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, label: str=None, type: str=None, date: str=None):
        """
        Annotation - a model defined in Swagger

        :param id: The id of this Annotation.
        :type id: str
        :param label: The label of this Annotation.
        :type label: str
        :param type: The type of this Annotation.
        :type type: str
        :param date: The date of this Annotation.
        :type date: str
        """
        self.swagger_types = {
            'id': str,
            'label': str,
            'type': str,
            'date': str
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'date': 'date'
        }

        self._id = id
        self._label = label
        self._type = type
        self._date = date

    @classmethod
    def from_dict(cls, dikt) -> 'Annotation':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Annotation of this Annotation.
        :rtype: Annotation
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Annotation.
        CURIE-encoded identifier to an associated external resources (e.g. PMID of a pubmed citation) 

        :return: The id of this Annotation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Annotation.
        CURIE-encoded identifier to an associated external resources (e.g. PMID of a pubmed citation) 

        :param id: The id of this Annotation.
        :type id: str
        """

        self._id = id

    @property
    def label(self) -> str:
        """
        Gets the label of this Annotation.
        canonical human readable and searchable label of the annotation (i.e. comment, matched sentence, etc.) 

        :return: The label of this Annotation.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """
        Sets the label of this Annotation.
        canonical human readable and searchable label of the annotation (i.e. comment, matched sentence, etc.) 

        :param label: The label of this Annotation.
        :type label: str
        """

        self._label = label

    @property
    def type(self) -> str:
        """
        Gets the type of this Annotation.
        Gene Ontology Evidence Code (http://www.geneontology.org/page/guide-go-evidence-codes) 

        :return: The type of this Annotation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Annotation.
        Gene Ontology Evidence Code (http://www.geneontology.org/page/guide-go-evidence-codes) 

        :param type: The type of this Annotation.
        :type type: str
        """

        self._type = type

    @property
    def date(self) -> str:
        """
        Gets the date of this Annotation.
        publication date of annotation (generally of format 'yyyy-mm-dd') 

        :return: The date of this Annotation.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """
        Sets the date of this Annotation.
        publication date of annotation (generally of format 'yyyy-mm-dd') 

        :param date: The date of this Annotation.
        :type date: str
        """

        self._date = date

