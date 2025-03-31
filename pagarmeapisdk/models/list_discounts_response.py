# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_discount_response import GetDiscountResponse
from pagarmeapisdk.models.paging_response import PagingResponse


class ListDiscountsResponse(object):

    """Implementation of the 'ListDiscountsResponse' model.

    Attributes:
        data (List[GetDiscountResponse]): The Discounts response
        paging (PagingResponse): Paging object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "paging": 'paging'
    }

    _optionals = [
        'data',
        'paging',
    ]

    _nullables = [
        'data',
        'paging',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 paging=APIHelper.SKIP):
        """Constructor for the ListDiscountsResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        if paging is not APIHelper.SKIP:
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
        if 'data' in dictionary.keys():
            data = [GetDiscountResponse.from_dictionary(x) for x in dictionary.get('data')] if dictionary.get('data') else None
        else:
            data = APIHelper.SKIP
        if 'paging' in dictionary.keys():
            paging = PagingResponse.from_dictionary(dictionary.get('paging')) if dictionary.get('paging') else None
        else:
            paging = APIHelper.SKIP
        # Return an object of this model
        return cls(data,
                   paging)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'data={(self.data if hasattr(self, "data") else None)!r}, '
                f'paging={(self.paging if hasattr(self, "paging") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'data={(self.data if hasattr(self, "data") else None)!s}, '
                f'paging={(self.paging if hasattr(self, "paging") else None)!s})')
