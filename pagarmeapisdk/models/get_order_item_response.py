# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetOrderItemResponse(object):

    """Implementation of the 'GetOrderItemResponse' model.

    Response object for getting an order item

    Attributes:
        id (str): Id
        mtype (str): The model property of type str.
        description (str): The model property of type str.
        amount (int): The model property of type int.
        quantity (int): The model property of type int.
        category (str): Category
        code (str): Code
        status (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "mtype": 'type',
        "description": 'description',
        "amount": 'amount',
        "quantity": 'quantity',
        "category": 'category',
        "code": 'code',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'id',
        'mtype',
        'description',
        'amount',
        'quantity',
        'category',
        'code',
        'status',
        'created_at',
        'updated_at',
    ]

    _nullables = [
        'id',
        'mtype',
        'description',
        'amount',
        'quantity',
        'category',
        'code',
        'status',
        'created_at',
        'updated_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP):
        """Constructor for the GetOrderItemResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if description is not APIHelper.SKIP:
            self.description = description 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if category is not APIHelper.SKIP:
            self.category = category 
        if code is not APIHelper.SKIP:
            self.code = code 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 

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
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        amount = dictionary.get("amount") if "amount" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("quantity") if "quantity" in dictionary.keys() else APIHelper.SKIP
        category = dictionary.get("category") if "category" in dictionary.keys() else APIHelper.SKIP
        code = dictionary.get("code") if "code" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   mtype,
                   description,
                   amount,
                   quantity,
                   category,
                   code,
                   status,
                   created_at,
                   updated_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'category={(self.category if hasattr(self, "category") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'category={(self.category if hasattr(self, "category") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s})')
