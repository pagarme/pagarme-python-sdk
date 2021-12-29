# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateConfirmPaymentRequest(object):

    """Implementation of the 'CreateConfirmPaymentRequest' model.

    TODO: type model description here.

    Attributes:
        description (string): Description
        amount (int): Amount
        code (string): Code reference

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "code": 'Code',
        "amount": 'Amount'
    }

    def __init__(self,
                 description=None,
                 code=None,
                 amount=None):
        """Constructor for the CreateConfirmPaymentRequest class"""

        # Initialize members of the class
        self.description = description
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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        description = dictionary.get('description')
        code = dictionary.get('Code')
        amount = dictionary.get('Amount')

        # Return an object of this model
        return cls(description,
                   code,
                   amount)