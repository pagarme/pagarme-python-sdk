# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.pix_additional_information import PixAdditionalInformation


class CreateCheckoutPixPaymentRequest(object):

    """Implementation of the 'CreateCheckoutPixPaymentRequest' model.

    Checkout pix payment request

    Attributes:
        expires_at (datetime): Expires at
        expires_in (int): Expires in
        additional_information (List[PixAdditionalInformation]): Additional
            information

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_at": 'expires_at',
        "expires_in": 'expires_in',
        "additional_information": 'additional_information'
    }

    _optionals = [
        'expires_at',
        'expires_in',
        'additional_information',
    ]

    def __init__(self,
                 expires_at=APIHelper.SKIP,
                 expires_in=APIHelper.SKIP,
                 additional_information=APIHelper.SKIP):
        """Constructor for the CreateCheckoutPixPaymentRequest class"""

        # Initialize members of the class
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
        if expires_in is not APIHelper.SKIP:
            self.expires_in = expires_in 
        if additional_information is not APIHelper.SKIP:
            self.additional_information = additional_information 

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
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else APIHelper.SKIP
        expires_in = dictionary.get("expires_in") if dictionary.get("expires_in") else APIHelper.SKIP
        additional_information = None
        if dictionary.get('additional_information') is not None:
            additional_information = [PixAdditionalInformation.from_dictionary(x) for x in dictionary.get('additional_information')]
        else:
            additional_information = APIHelper.SKIP
        # Return an object of this model
        return cls(expires_at,
                   expires_in,
                   additional_information)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!r}, '
                f'expires_in={(self.expires_in if hasattr(self, "expires_in") else None)!r}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!s}, '
                f'expires_in={(self.expires_in if hasattr(self, "expires_in") else None)!s}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!s})')
