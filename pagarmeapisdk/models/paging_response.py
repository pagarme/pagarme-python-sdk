# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class PagingResponse(object):

    """Implementation of the 'PagingResponse' model.

    Object used for returning lists of objects with pagination

    Attributes:
        total (int): Total number of pages
        previous (str): Previous page
        next (str): Next page

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total": 'total',
        "previous": 'previous',
        "next": 'next'
    }

    _optionals = [
        'total',
        'previous',
        'next',
    ]

    _nullables = [
        'total',
        'previous',
        'next',
    ]

    def __init__(self,
                 total=APIHelper.SKIP,
                 previous=APIHelper.SKIP,
                 next=APIHelper.SKIP):
        """Constructor for the PagingResponse class"""

        # Initialize members of the class
        if total is not APIHelper.SKIP:
            self.total = total 
        if previous is not APIHelper.SKIP:
            self.previous = previous 
        if next is not APIHelper.SKIP:
            self.next = next 

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
        total = dictionary.get("total") if "total" in dictionary.keys() else APIHelper.SKIP
        previous = dictionary.get("previous") if "previous" in dictionary.keys() else APIHelper.SKIP
        next = dictionary.get("next") if "next" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(total,
                   previous,
                   next)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'total={(self.total if hasattr(self, "total") else None)!r}, '
                f'previous={(self.previous if hasattr(self, "previous") else None)!r}, '
                f'next={(self.next if hasattr(self, "next") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'total={(self.total if hasattr(self, "total") else None)!s}, '
                f'previous={(self.previous if hasattr(self, "previous") else None)!s}, '
                f'next={(self.next if hasattr(self, "next") else None)!s})')
