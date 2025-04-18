# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest


class CreatePlanItemRequest(object):

    """Implementation of the 'CreatePlanItemRequest' model.

    Request for creating a plan item

    Attributes:
        name (str): Item name
        pricing_scheme (CreatePricingSchemeRequest): Item's pricing scheme
        id (str): Item's id
        description (str): Item's description
        cycles (int): Number of cycles where the item will be charged
        quantity (int): Quantity

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "pricing_scheme": 'pricing_scheme',
        "id": 'id',
        "description": 'description',
        "cycles": 'cycles',
        "quantity": 'quantity'
    }

    _optionals = [
        'cycles',
        'quantity',
    ]

    def __init__(self,
                 name=None,
                 pricing_scheme=None,
                 id=None,
                 description=None,
                 cycles=APIHelper.SKIP,
                 quantity=APIHelper.SKIP):
        """Constructor for the CreatePlanItemRequest class"""

        # Initialize members of the class
        self.name = name 
        self.pricing_scheme = pricing_scheme 
        self.id = id 
        self.description = description 
        if cycles is not APIHelper.SKIP:
            self.cycles = cycles 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        pricing_scheme = CreatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        id = dictionary.get("id") if dictionary.get("id") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        cycles = dictionary.get("cycles") if dictionary.get("cycles") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   pricing_scheme,
                   id,
                   description,
                   cycles,
                   quantity)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'id={self.id!r}, '
                f'description={self.description!r}, '
                f'cycles={(self.cycles if hasattr(self, "cycles") else None)!r}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'id={self.id!s}, '
                f'description={self.description!s}, '
                f'cycles={(self.cycles if hasattr(self, "cycles") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s})')
