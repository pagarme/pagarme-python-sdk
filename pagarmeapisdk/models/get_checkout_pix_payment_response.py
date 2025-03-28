# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.pix_additional_information import PixAdditionalInformation


class GetCheckoutPixPaymentResponse(object):

    """Implementation of the 'GetCheckoutPixPaymentResponse' model.

    Checkout pix payment response

    Attributes:
        expires_at (datetime): Expires at
        additional_information (List[PixAdditionalInformation]): Additional
            information

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_at": 'expires_at',
        "additional_information": 'additional_information'
    }

    _optionals = [
        'expires_at',
        'additional_information',
    ]

    _nullables = [
        'expires_at',
        'additional_information',
    ]

    def __init__(self,
                 expires_at=APIHelper.SKIP,
                 additional_information=APIHelper.SKIP):
        """Constructor for the GetCheckoutPixPaymentResponse class"""

        # Initialize members of the class
        if expires_at is not APIHelper.SKIP:
            self.expires_at = APIHelper.apply_datetime_converter(expires_at, APIHelper.RFC3339DateTime) if expires_at else None 
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
        if 'expires_at' in dictionary.keys():
            expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else None
        else:
            expires_at = APIHelper.SKIP
        if 'additional_information' in dictionary.keys():
            additional_information = [PixAdditionalInformation.from_dictionary(x) for x in dictionary.get('additional_information')] if dictionary.get('additional_information') else None
        else:
            additional_information = APIHelper.SKIP
        # Return an object of this model
        return cls(expires_at,
                   additional_information)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!r}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'expires_at={(self.expires_at if hasattr(self, "expires_at") else None)!s}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!s})')
