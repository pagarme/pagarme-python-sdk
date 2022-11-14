# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GetInterestResponse(object):

    """Implementation of the 'GetInterestResponse' model.

    Interest Response

    Attributes:
        days (int): Days
        mtype (string): Type
        amount (int): Amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days": 'days',
        "mtype": 'type',
        "amount": 'amount'
    }

    def __init__(self,
                 days=None,
                 mtype=None,
                 amount=None):
        """Constructor for the GetInterestResponse class"""

        # Initialize members of the class
        self.days = days 
        self.mtype = mtype 
        self.amount = amount 

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

        days = dictionary.get("days") if dictionary.get("days") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        # Return an object of this model
        return cls(days,
                   mtype,
                   amount)