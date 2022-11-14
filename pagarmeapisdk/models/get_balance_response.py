# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse


class GetBalanceResponse(object):

    """Implementation of the 'GetBalanceResponse' model.

    Balance

    Attributes:
        currency (string): Currency
        available_amount (long|int): Amount available for transferring
        recipient (GetRecipientResponse): Recipient
        transferred_amount (long|int): TODO: type description here.
        waiting_funds_amount (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "available_amount": 'available_amount',
        "transferred_amount": 'transferred_amount',
        "waiting_funds_amount": 'waiting_funds_amount',
        "recipient": 'recipient'
    }

    _optionals = [
        'recipient',
    ]

    def __init__(self,
                 currency=None,
                 available_amount=None,
                 transferred_amount=None,
                 waiting_funds_amount=None,
                 recipient=APIHelper.SKIP):
        """Constructor for the GetBalanceResponse class"""

        # Initialize members of the class
        self.currency = currency 
        self.available_amount = available_amount 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        self.transferred_amount = transferred_amount 
        self.waiting_funds_amount = waiting_funds_amount 

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

        currency = dictionary.get("currency") if dictionary.get("currency") else None
        available_amount = dictionary.get("available_amount") if dictionary.get("available_amount") else None
        transferred_amount = dictionary.get("transferred_amount") if dictionary.get("transferred_amount") else None
        waiting_funds_amount = dictionary.get("waiting_funds_amount") if dictionary.get("waiting_funds_amount") else None
        recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if 'recipient' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(currency,
                   available_amount,
                   transferred_amount,
                   waiting_funds_amount,
                   recipient)
