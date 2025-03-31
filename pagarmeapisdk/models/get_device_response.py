# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetDeviceResponse(object):

    """Implementation of the 'GetDeviceResponse' model.

    Response object for geetting an order device

    Attributes:
        platform (str): Device's platform name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "platform": 'platform'
    }

    _optionals = [
        'platform',
    ]

    _nullables = [
        'platform',
    ]

    def __init__(self,
                 platform=APIHelper.SKIP):
        """Constructor for the GetDeviceResponse class"""

        # Initialize members of the class
        if platform is not APIHelper.SKIP:
            self.platform = platform 

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
        platform = dictionary.get("platform") if "platform" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(platform)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'platform={(self.platform if hasattr(self, "platform") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'platform={(self.platform if hasattr(self, "platform") else None)!s})')
