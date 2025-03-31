# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest


class CreateCheckoutDebitCardPaymentRequest(object):

    """Implementation of the 'CreateCheckoutDebitCardPaymentRequest' model.

    Checkout credit card payment request

    Attributes:
        statement_descriptor (str): Card invoice text descriptor
        authentication (CreatePaymentAuthenticationRequest): Creates payment
            authentication

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authentication": 'authentication',
        "statement_descriptor": 'statement_descriptor'
    }

    _optionals = [
        'statement_descriptor',
    ]

    def __init__(self,
                 authentication=None,
                 statement_descriptor=APIHelper.SKIP):
        """Constructor for the CreateCheckoutDebitCardPaymentRequest class"""

        # Initialize members of the class
        if statement_descriptor is not APIHelper.SKIP:
            self.statement_descriptor = statement_descriptor 
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
        authentication = CreatePaymentAuthenticationRequest.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        statement_descriptor = dictionary.get("statement_descriptor") if dictionary.get("statement_descriptor") else APIHelper.SKIP
        # Return an object of this model
        return cls(authentication,
                   statement_descriptor)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!r}, '
                f'authentication={self.authentication!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'statement_descriptor={(self.statement_descriptor if hasattr(self, "statement_descriptor") else None)!s}, '
                f'authentication={self.authentication!s})')
