# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateFineRequest(object):

    """Implementation of the 'CreateFineRequest' model.

    Fine Request

    Attributes:
        days (int): Days
        mtype (str): Type
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
        """Constructor for the CreateFineRequest class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        days = dictionary.get("days") if dictionary.get("days") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        # Return an object of this model
        return cls(days,
                   mtype,
                   amount)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'days={self.days!r}, '
                f'mtype={self.mtype!r}, '
                f'amount={self.amount!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'days={self.days!s}, '
                f'mtype={self.mtype!s}, '
                f'amount={self.amount!s})')
