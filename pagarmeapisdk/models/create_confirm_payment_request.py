# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateConfirmPaymentRequest(object):

    """Implementation of the 'CreateConfirmPaymentRequest' model.

    Attributes:
        description (str): Description
        amount (int): Amount
        code (str): Code reference

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "code": 'Code',
        "amount": 'Amount'
    }

    _optionals = [
        'amount',
    ]

    def __init__(self,
                 description=None,
                 code=None,
                 amount=APIHelper.SKIP):
        """Constructor for the CreateConfirmPaymentRequest class"""

        # Initialize members of the class
        self.description = description 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        self.code = code 

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
        description = dictionary.get("description") if dictionary.get("description") else None
        code = dictionary.get("Code") if dictionary.get("Code") else None
        amount = dictionary.get("Amount") if dictionary.get("Amount") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   code,
                   amount)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'code={self.code!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'code={self.code!s})')
