# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateCheckoutBoletoPaymentRequest(object):

    """Implementation of the 'CreateCheckoutBoletoPaymentRequest' model.

    Attributes:
        bank (str): Bank identifier
        instructions (str): Instructions
        due_at (datetime): Due date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank": 'bank',
        "instructions": 'instructions',
        "due_at": 'due_at'
    }

    def __init__(self,
                 bank=None,
                 instructions=None,
                 due_at=None):
        """Constructor for the CreateCheckoutBoletoPaymentRequest class"""

        # Initialize members of the class
        self.bank = bank 
        self.instructions = instructions 
        self.due_at = APIHelper.apply_datetime_converter(due_at, APIHelper.RFC3339DateTime) if due_at else None 

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
        bank = dictionary.get("bank") if dictionary.get("bank") else None
        instructions = dictionary.get("instructions") if dictionary.get("instructions") else None
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None
        # Return an object of this model
        return cls(bank,
                   instructions,
                   due_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'bank={self.bank!r}, '
                f'instructions={self.instructions!r}, '
                f'due_at={self.due_at!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'bank={self.bank!s}, '
                f'instructions={self.instructions!s}, '
                f'due_at={self.due_at!s})')
