# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_card_token_request import CreateCardTokenRequest


class CreateTokenRequest(object):

    """Implementation of the 'CreateTokenRequest' model.

    Token data

    Attributes:
        mtype (string): Token type
        card (CreateCardTokenRequest): Card data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "card": 'card'
    }

    def __init__(self,
                 mtype='card',
                 card=None):
        """Constructor for the CreateTokenRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.card = card 

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

        mtype = dictionary.get("type") if dictionary.get("type") else 'card'
        card = CreateCardTokenRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        # Return an object of this model
        return cls(mtype,
                   card)
