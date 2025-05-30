# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_discount_request import CreateDiscountRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest


class CreateSubscriptionItemRequest(object):

    """Implementation of the 'CreateSubscriptionItemRequest' model.

    Request for creating a new subscription item

    Attributes:
        description (str): Item description
        pricing_scheme (CreatePricingSchemeRequest): Pricing scheme
        id (str): Item id
        plan_item_id (str): Plan item id
        discounts (List[CreateDiscountRequest]): Discounts for the item
        name (str): Item name
        cycles (int): Number of cycles which the item will be charged
        quantity (int): Quantity of items
        minimum_price (int): Minimum price

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "pricing_scheme": 'pricing_scheme',
        "id": 'id',
        "plan_item_id": 'plan_item_id',
        "discounts": 'discounts',
        "name": 'name',
        "cycles": 'cycles',
        "quantity": 'quantity',
        "minimum_price": 'minimum_price'
    }

    _optionals = [
        'cycles',
        'quantity',
        'minimum_price',
    ]

    def __init__(self,
                 description=None,
                 pricing_scheme=None,
                 id=None,
                 plan_item_id=None,
                 discounts=None,
                 name=None,
                 cycles=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 minimum_price=APIHelper.SKIP):
        """Constructor for the CreateSubscriptionItemRequest class"""

        # Initialize members of the class
        self.description = description 
        self.pricing_scheme = pricing_scheme 
        self.id = id 
        self.plan_item_id = plan_item_id 
        self.discounts = discounts 
        self.name = name 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 

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
        description = dictionary.get("description") if dictionary.get("description") else None
        pricing_scheme = CreatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        id = dictionary.get("id") if dictionary.get("id") else None
        plan_item_id = dictionary.get("plan_item_id") if dictionary.get("plan_item_id") else None
        discounts = None
        if dictionary.get('discounts') is not None:
            discounts = [CreateDiscountRequest.from_dictionary(x) for x in dictionary.get('discounts')]
        name = dictionary.get("name") if dictionary.get("name") else None
        cycles = dictionary.get("cycles") if dictionary.get("cycles") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        minimum_price = dictionary.get("minimum_price") if dictionary.get("minimum_price") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   pricing_scheme,
                   id,
                   plan_item_id,
                   discounts,
                   name,
                   cycles,
                   quantity,
                   minimum_price)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'id={self.id!r}, '
                f'plan_item_id={self.plan_item_id!r}, '
                f'discounts={self.discounts!r}, '
                f'name={self.name!r}, '
                f'cycles={(self.cycles if hasattr(self, "cycles") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'minimum_price={(self.minimum_price if hasattr(self, "minimum_price") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'id={self.id!s}, '
                f'plan_item_id={self.plan_item_id!s}, '
                f'discounts={self.discounts!s}, '
                f'name={self.name!s}, '
                f'cycles={(self.cycles if hasattr(self, "cycles") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'minimum_price={(self.minimum_price if hasattr(self, "minimum_price") else None)!s})')
