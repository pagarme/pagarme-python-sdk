# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_clear_sale_request import CreateClearSaleRequest


class CreateAntifraudRequest(object):

    """Implementation of the 'CreateAntifraudRequest' model.

    Attributes:
        mtype (str): The model property of type str.
        clearsale (CreateClearSaleRequest): The model property of type
            CreateClearSaleRequest.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "clearsale": 'clearsale'
    }

    def __init__(self,
                 mtype=None,
                 clearsale=None):
        """Constructor for the CreateAntifraudRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.clearsale = clearsale 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        mtype = dictionary.get("type") if dictionary.get("type") else None
        clearsale = CreateClearSaleRequest.from_dictionary(dictionary.get('clearsale')) if dictionary.get('clearsale') else None
        # Return an object of this model
        return cls(mtype,
                   clearsale)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!r}, '
                f'clearsale={self.clearsale!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!s}, '
                f'clearsale={self.clearsale!s})')
