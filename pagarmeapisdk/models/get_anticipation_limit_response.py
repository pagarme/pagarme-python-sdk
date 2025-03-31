# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetAnticipationLimitResponse(object):

    """Implementation of the 'GetAnticipationLimitResponse' model.

    Anticipation limit

    Attributes:
        amount (int): Amount
        anticipation_fee (int): Anticipation fee

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "anticipation_fee": 'anticipation_fee'
    }

    _optionals = [
        'amount',
        'anticipation_fee',
    ]

    _nullables = [
        'amount',
        'anticipation_fee',
    ]

    def __init__(self,
                 amount=APIHelper.SKIP,
                 anticipation_fee=APIHelper.SKIP):
        """Constructor for the GetAnticipationLimitResponse class"""

        # Initialize members of the class
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if anticipation_fee is not APIHelper.SKIP:
            self.anticipation_fee = anticipation_fee 

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
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        anticipation_fee = dictionary.get("anticipation_fee") if "anticipation_fee" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount,
                   anticipation_fee)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'anticipation_fee={(self.anticipation_fee if hasattr(self, "anticipation_fee") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'anticipation_fee={(self.anticipation_fee if hasattr(self, "anticipation_fee") else None)!s})')
