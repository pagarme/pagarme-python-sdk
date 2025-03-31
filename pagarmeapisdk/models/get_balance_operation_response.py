# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectBaseResponse


class GetBalanceOperationResponse(object):

    """Implementation of the 'GetBalanceOperationResponse' model.

    Generic response object for getting a BalanceOperation.

    Attributes:
        id (str): The model property of type str.
        status (str): The model property of type str.
        balance_amount (str): The model property of type str.
        balance_old_amount (str): The model property of type str.
        mtype (str): The model property of type str.
        amount (int): The model property of type int.
        fee (str): The model property of type str.
        created_at (str): The model property of type str.
        movement_object (GetMovementObjectBaseResponse): The model property of
            type GetMovementObjectBaseResponse.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "status": 'status',
        "balance_amount": 'balance_amount',
        "balance_old_amount": 'balance_old_amount',
        "mtype": 'type',
        "amount": 'amount',
        "fee": 'fee',
        "created_at": 'created_at',
        "movement_object": 'movement_object'
    }

    _optionals = [
        'id',
        'status',
        'balance_amount',
        'balance_old_amount',
        'mtype',
        'amount',
        'fee',
        'created_at',
        'movement_object',
    ]

    _nullables = [
        'id',
        'status',
        'balance_amount',
        'balance_old_amount',
        'mtype',
        'amount',
        'fee',
        'created_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 balance_amount=APIHelper.SKIP,
                 balance_old_amount=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 fee=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 movement_object=APIHelper.SKIP):
        """Constructor for the GetBalanceOperationResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if balance_amount is not APIHelper.SKIP:
            self.balance_amount = balance_amount 
        if balance_old_amount is not APIHelper.SKIP:
            self.balance_old_amount = balance_old_amount 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if fee is not APIHelper.SKIP:
            self.fee = fee 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if movement_object is not APIHelper.SKIP:
            self.movement_object = movement_object 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        balance_amount = dictionary.get("balance_amount") if "balance_amount" in dictionary.keys() else APIHelper.SKIP
        balance_old_amount = dictionary.get("balance_old_amount") if "balance_old_amount" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        fee = dictionary.get("fee") if "fee" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        movement_object = GetMovementObjectBaseResponse.from_dictionary(dictionary.get('movement_object')) if 'movement_object' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   status,
                   balance_amount,
                   balance_old_amount,
                   mtype,
                   amount,
                   fee,
                   created_at,
                   movement_object)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'balance_amount={(self.balance_amount if hasattr(self, "balance_amount") else None)!r}, '
                f'balance_old_amount={(self.balance_old_amount if hasattr(self, "balance_old_amount") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'fee={(self.fee if hasattr(self, "fee") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'movement_object={(self.movement_object if hasattr(self, "movement_object") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'balance_amount={(self.balance_amount if hasattr(self, "balance_amount") else None)!s}, '
                f'balance_old_amount={(self.balance_old_amount if hasattr(self, "balance_old_amount") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'fee={(self.fee if hasattr(self, "fee") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'movement_object={(self.movement_object if hasattr(self, "movement_object") else None)!s})')
