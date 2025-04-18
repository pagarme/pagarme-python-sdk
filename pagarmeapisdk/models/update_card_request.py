# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_address_request import CreateAddressRequest


class UpdateCardRequest(object):

    """Implementation of the 'UpdateCardRequest' model.

    Request for updating a card

    Attributes:
        holder_name (str): Holder name
        exp_month (int): Expiration month
        exp_year (int): Expiration year
        billing_address_id (str): Id of the address to be used as billing
            address
        billing_address (CreateAddressRequest): Billing address
        metadata (Dict[str, str]): Metadata
        label (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "holder_name": 'holder_name',
        "exp_month": 'exp_month',
        "exp_year": 'exp_year',
        "billing_address": 'billing_address',
        "metadata": 'metadata',
        "label": 'label',
        "billing_address_id": 'billing_address_id'
    }

    _optionals = [
        'billing_address_id',
    ]

    _nullables = [
        'billing_address_id',
    ]

    def __init__(self,
                 holder_name=None,
                 exp_month=None,
                 exp_year=None,
                 billing_address=None,
                 metadata=None,
                 label=None,
                 billing_address_id=APIHelper.SKIP):
        """Constructor for the UpdateCardRequest class"""

        # Initialize members of the class
        self.holder_name = holder_name 
        self.exp_month = exp_month 
        self.exp_year = exp_year 
        if billing_address_id is not APIHelper.SKIP:
            self.billing_address_id = billing_address_id 
        self.billing_address = billing_address 
        self.metadata = metadata 
        self.label = label 

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
        holder_name = dictionary.get("holder_name") if dictionary.get("holder_name") else None
        exp_month = dictionary.get("exp_month") if dictionary.get("exp_month") else None
        exp_year = dictionary.get("exp_year") if dictionary.get("exp_year") else None
        billing_address = CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        label = dictionary.get("label") if dictionary.get("label") else None
        billing_address_id = dictionary.get("billing_address_id") if "billing_address_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(holder_name,
                   exp_month,
                   exp_year,
                   billing_address,
                   metadata,
                   label,
                   billing_address_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'holder_name={self.holder_name!r}, '
                f'exp_month={self.exp_month!r}, '
                f'exp_year={self.exp_year!r}, '
                f'billing_address_id={(self.billing_address_id if hasattr(self, "billing_address_id") else None)!r}, '
                f'billing_address={self.billing_address!r}, '
                f'metadata={self.metadata!r}, '
                f'label={self.label!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'holder_name={self.holder_name!s}, '
                f'exp_month={self.exp_month!s}, '
                f'exp_year={self.exp_year!s}, '
                f'billing_address_id={(self.billing_address_id if hasattr(self, "billing_address_id") else None)!s}, '
                f'billing_address={self.billing_address!s}, '
                f'metadata={self.metadata!s}, '
                f'label={self.label!s})')
