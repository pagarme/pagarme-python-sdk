# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateKYCLinkResponse(object):

    """Implementation of the 'CreateKYCLinkResponse' model.

    KYC Link

    Attributes:
        base_64 (str): Base64
        url (str): URL
        expiration_date (str): Expiration Date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base_64": 'base64',
        "url": 'url',
        "expiration_date": 'expiration_date'
    }

    _optionals = [
        'base_64',
        'url',
        'expiration_date',
    ]

    _nullables = [
        'base_64',
        'url',
        'expiration_date',
    ]

    def __init__(self,
                 base_64=APIHelper.SKIP,
                 url=APIHelper.SKIP,
                 expiration_date=APIHelper.SKIP):
        """Constructor for the CreateKYCLinkResponse class"""

        # Initialize members of the class
        if base_64 is not APIHelper.SKIP:
            self.base_64 = base_64 
        if url is not APIHelper.SKIP:
            self.url = url 
        if expiration_date is not APIHelper.SKIP:
            self.expiration_date = expiration_date 

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
        base_64 = dictionary.get("base64") if "base64" in dictionary.keys() else APIHelper.SKIP
        url = dictionary.get("url") if "url" in dictionary.keys() else APIHelper.SKIP
        expiration_date = dictionary.get("expiration_date") if "expiration_date" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(base_64,
                   url,
                   expiration_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'base_64={(self.base_64 if hasattr(self, "base_64") else None)!r}, '
                f'url={(self.url if hasattr(self, "url") else None)!r}, '
                f'expiration_date={(self.expiration_date if hasattr(self, "expiration_date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'base_64={(self.base_64 if hasattr(self, "base_64") else None)!s}, '
                f'url={(self.url if hasattr(self, "url") else None)!s}, '
                f'expiration_date={(self.expiration_date if hasattr(self, "expiration_date") else None)!s})')
