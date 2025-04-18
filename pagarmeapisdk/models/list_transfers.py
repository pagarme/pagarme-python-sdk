# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.get_transfer import GetTransfer
from pagarmeapisdk.models.paging_response import PagingResponse


class ListTransfers(object):

    """Implementation of the 'ListTransfers' model.

    Attributes:
        data (List[GetTransfer]): The Increments response
        paging (PagingResponse): Paging object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "paging": 'paging'
    }

    def __init__(self,
                 data=None,
                 paging=None):
        """Constructor for the ListTransfers class"""

        # Initialize members of the class
        self.data = data 
        self.paging = paging 

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
        data = None
        if dictionary.get('data') is not None:
            data = [GetTransfer.from_dictionary(x) for x in dictionary.get('data')]
        paging = PagingResponse.from_dictionary(dictionary.get('paging')) if dictionary.get('paging') else None
        # Return an object of this model
        return cls(data,
                   paging)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'data={self.data!r}, '
                f'paging={self.paging!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'data={self.data!s}, '
                f'paging={self.paging!s})')
