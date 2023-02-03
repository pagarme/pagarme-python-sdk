# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse
from pagarmeapisdk.models.get_split_options_response import GetSplitOptionsResponse


class GetSplitResponse(object):

    """Implementation of the 'GetSplitResponse' model.

    Split response

    Attributes:
        mtype (string): Type
        amount (int): Amount
        recipient (GetRecipientResponse): Recipient
        gateway_id (string): The split rule gateway id
        options (GetSplitOptionsResponse): TODO: type description here.
        id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "amount": 'amount',
        "recipient": 'recipient',
        "gateway_id": 'gateway_id',
        "options": 'options',
        "id": 'id'
    }

    _optionals = [
        'mtype',
        'amount',
        'recipient',
        'gateway_id',
        'options',
        'id',
    ]

    _nullables = [
        'mtype',
        'amount',
        'recipient',
        'gateway_id',
        'options',
        'id',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 recipient=APIHelper.SKIP,
                 gateway_id=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 id=APIHelper.SKIP):
        """Constructor for the GetSplitResponse class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        if gateway_id is not APIHelper.SKIP:
            self.gateway_id = gateway_id 
        if options is not APIHelper.SKIP:
            self.options = options 
        if id is not APIHelper.SKIP:
            self.id = id 

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

        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        if 'recipient' in dictionary.keys():
            recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None
        else:
            recipient = APIHelper.SKIP
        gateway_id = dictionary.get("gateway_id") if "gateway_id" in dictionary.keys() else APIHelper.SKIP
        if 'options' in dictionary.keys():
            options = GetSplitOptionsResponse.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None
        else:
            options = APIHelper.SKIP
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   amount,
                   recipient,
                   gateway_id,
                   options,
                   id)
