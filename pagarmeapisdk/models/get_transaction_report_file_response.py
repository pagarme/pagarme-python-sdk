# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetTransactionReportFileResponse(object):

    """Implementation of the 'GetTransactionReportFileResponse' model.

    Attributes:
        name (str): The model property of type str.
        date (datetime): The model property of type datetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "date": 'date'
    }

    _optionals = [
        'name',
        'date',
    ]

    _nullables = [
        'name',
        'date',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 date=APIHelper.SKIP):
        """Constructor for the GetTransactionReportFileResponse class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if date is not APIHelper.SKIP:
            self.date = APIHelper.apply_datetime_converter(date, APIHelper.RFC3339DateTime) if date else None 

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
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        if 'date' in dictionary.keys():
            date = APIHelper.RFC3339DateTime.from_value(dictionary.get("date")).datetime if dictionary.get("date") else None
        else:
            date = APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'date={(self.date if hasattr(self, "date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'date={(self.date if hasattr(self, "date") else None)!s})')
