# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_gateway_error_response import GetGatewayErrorResponse


class GetGatewayResponseResponse(object):

    """Implementation of the 'GetGatewayResponseResponse' model.

    The Transaction Gateway Response

    Attributes:
        code (str): The error code
        errors (List[GetGatewayErrorResponse]): The gateway response errors
            list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "errors": 'errors'
    }

    _optionals = [
        'code',
        'errors',
    ]

    _nullables = [
        'code',
        'errors',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 errors=APIHelper.SKIP):
        """Constructor for the GetGatewayResponseResponse class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if errors is not APIHelper.SKIP:
            self.errors = errors 

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
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        if 'errors' in dictionary.keys():
            errors = [GetGatewayErrorResponse.from_dictionary(x) for x in dictionary.get('errors')] if dictionary.get('errors') else None
        else:
            errors = APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   errors)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!s})')
