# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetGatewayErrorResponse(object):

    """Implementation of the 'GetGatewayErrorResponse' model.

    Gateway Response

    Attributes:
        message (str): The message error

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message'
    }

    _optionals = [
        'message',
    ]

    _nullables = [
        'message',
    ]

    def __init__(self,
                 message=APIHelper.SKIP):
        """Constructor for the GetGatewayErrorResponse class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 

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
        message = dictionary.get("message") if "message" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(message)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'message={(self.message if hasattr(self, "message") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'message={(self.message if hasattr(self, "message") else None)!s})')
