# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_apple_pay_header_request import CreateApplePayHeaderRequest


class CreateApplePayRequest(object):

    """Implementation of the 'CreateApplePayRequest' model.

    The ApplePay Token Payment Request

    Attributes:
        version (str): The token version
        data (str): The cryptography data
        header (CreateApplePayHeaderRequest): The ApplePay header request
        signature (str): Detached PKCS #7 signature, Base64 encoded as string
        merchant_identifier (str): ApplePay Merchant identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": 'version',
        "data": 'data',
        "header": 'header',
        "signature": 'signature',
        "merchant_identifier": 'merchant_identifier'
    }

    def __init__(self,
                 version=None,
                 data=None,
                 header=None,
                 signature=None,
                 merchant_identifier=None):
        """Constructor for the CreateApplePayRequest class"""

        # Initialize members of the class
        self.version = version 
        self.data = data 
        self.header = header 
        self.signature = signature 
        self.merchant_identifier = merchant_identifier 

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
        version = dictionary.get("version") if dictionary.get("version") else None
        data = dictionary.get("data") if dictionary.get("data") else None
        header = CreateApplePayHeaderRequest.from_dictionary(dictionary.get('header')) if dictionary.get('header') else None
        signature = dictionary.get("signature") if dictionary.get("signature") else None
        merchant_identifier = dictionary.get("merchant_identifier") if dictionary.get("merchant_identifier") else None
        # Return an object of this model
        return cls(version,
                   data,
                   header,
                   signature,
                   merchant_identifier)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'version={self.version!r}, '
                f'data={self.data!r}, '
                f'header={self.header!r}, '
                f'signature={self.signature!r}, '
                f'merchant_identifier={self.merchant_identifier!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'version={self.version!s}, '
                f'data={self.data!s}, '
                f'header={self.header!s}, '
                f'signature={self.signature!s}, '
                f'merchant_identifier={self.merchant_identifier!s})')
