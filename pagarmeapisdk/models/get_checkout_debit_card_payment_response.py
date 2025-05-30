# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_payment_authentication_response import GetPaymentAuthenticationResponse


class GetCheckoutDebitCardPaymentResponse(object):

    """Implementation of the 'GetCheckoutDebitCardPaymentResponse' model.

    Attributes:
        statement_descriptor (str): Descrição na fatura
        authentication (GetPaymentAuthenticationResponse): Payment
            Authentication response object data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor": 'statement_descriptor',
        "authentication": 'authentication'
    }

    _optionals = [
        'statement_descriptor',
        'authentication',
    ]

    _nullables = [
        'statement_descriptor',
        'authentication',
    ]

    def __init__(self,
                 statement_descriptor=APIHelper.SKIP,
                 authentication=APIHelper.SKIP):
        """Constructor for the GetCheckoutDebitCardPaymentResponse class"""

        # Initialize members of the class
        if statement_descriptor is not APIHelper.SKIP:
            self.statement_descriptor = statement_descriptor 
        if authentication is not APIHelper.SKIP:
            self.authentication = authentication 

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
        statement_descriptor = dictionary.get("statement_descriptor") if "statement_descriptor" in dictionary.keys() else APIHelper.SKIP
        if 'authentication' in dictionary.keys():
            authentication = GetPaymentAuthenticationResponse.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        else:
            authentication = APIHelper.SKIP
        # Return an object of this model
        return cls(statement_descriptor,
                   authentication)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!r}, '
                f'authentication={(self.authentication if hasattr(self, "authentication") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!s}, '
                f'authentication={(self.authentication if hasattr(self, "authentication") else None)!s})')
