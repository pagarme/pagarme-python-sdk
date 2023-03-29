# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_card_options_request import CreateCardOptionsRequest


class CreateCardRequest(object):

    """Implementation of the 'CreateCardRequest' model.

    Card data

    Attributes:
        number (string): Credit card number
        holder_name (string): Holder name, as written on the card
        exp_month (int): The expiration month
        exp_year (int): The expiration year, that can be informed with 2 or 4
            digits
        cvv (string): The card's security code
        billing_address (CreateAddressRequest): Card's billing address
        brand (string): Card brand
        billing_address_id (string): The address id for the billing address
        metadata (dict): Metadata
        mtype (string): Card type
        options (CreateCardOptionsRequest): Options for creating the card
        holder_document (string): Document number for the card's holder
        private_label (bool): Indicates whether it is a private label card
        label (string): TODO: type description here.
        id (string): Identifier
        token (string): token identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number": 'number',
        "holder_name": 'holder_name',
        "exp_month": 'exp_month',
        "exp_year": 'exp_year',
        "cvv": 'cvv',
        "billing_address": 'billing_address',
        "brand": 'brand',
        "billing_address_id": 'billing_address_id',
        "metadata": 'metadata',
        "mtype": 'type',
        "options": 'options',
        "holder_document": 'holder_document',
        "private_label": 'private_label',
        "label": 'label',
        "id": 'id',
        "token": 'token'
    }

    _optionals = [
        'number',
        'holder_name',
        'exp_month',
        'exp_year',
        'cvv',
        'billing_address',
        'brand',
        'billing_address_id',
        'metadata',
        'mtype',
        'options',
        'holder_document',
        'private_label',
        'label',
        'id',
        'token',
    ]

    def __init__(self,
                 number=APIHelper.SKIP,
                 holder_name=APIHelper.SKIP,
                 exp_month=APIHelper.SKIP,
                 exp_year=APIHelper.SKIP,
                 cvv=APIHelper.SKIP,
                 billing_address=APIHelper.SKIP,
                 brand=APIHelper.SKIP,
                 billing_address_id=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 mtype='credit',
                 options=APIHelper.SKIP,
                 holder_document=APIHelper.SKIP,
                 private_label=APIHelper.SKIP,
                 label=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 token=APIHelper.SKIP):
        """Constructor for the CreateCardRequest class"""

        # Initialize members of the class
        if number is not APIHelper.SKIP:
            self.number = number 
        if holder_name is not APIHelper.SKIP:
            self.holder_name = holder_name 
        if exp_month is not APIHelper.SKIP:
            self.exp_month = exp_month 
        if exp_year is not APIHelper.SKIP:
            self.exp_year = exp_year 
        if cvv is not APIHelper.SKIP:
            self.cvv = cvv 
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address 
        if brand is not APIHelper.SKIP:
            self.brand = brand 
        if billing_address_id is not APIHelper.SKIP:
            self.billing_address_id = billing_address_id 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        self.mtype = mtype 
        if options is not APIHelper.SKIP:
            self.options = options 
        if holder_document is not APIHelper.SKIP:
            self.holder_document = holder_document 
        if private_label is not APIHelper.SKIP:
            self.private_label = private_label 
        if label is not APIHelper.SKIP:
            self.label = label 
        if id is not APIHelper.SKIP:
            self.id = id 
        if token is not APIHelper.SKIP:
            self.token = token 

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

        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        holder_name = dictionary.get("holder_name") if dictionary.get("holder_name") else APIHelper.SKIP
        exp_month = dictionary.get("exp_month") if dictionary.get("exp_month") else APIHelper.SKIP
        exp_year = dictionary.get("exp_year") if dictionary.get("exp_year") else APIHelper.SKIP
        cvv = dictionary.get("cvv") if dictionary.get("cvv") else APIHelper.SKIP
        billing_address = CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if 'billing_address' in dictionary.keys() else APIHelper.SKIP
        brand = dictionary.get("brand") if dictionary.get("brand") else APIHelper.SKIP
        billing_address_id = dictionary.get("billing_address_id") if dictionary.get("billing_address_id") else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'credit'
        options = CreateCardOptionsRequest.from_dictionary(dictionary.get('options')) if 'options' in dictionary.keys() else APIHelper.SKIP
        holder_document = dictionary.get("holder_document") if dictionary.get("holder_document") else APIHelper.SKIP
        private_label = dictionary.get("private_label") if "private_label" in dictionary.keys() else APIHelper.SKIP
        label = dictionary.get("label") if dictionary.get("label") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        token = dictionary.get("token") if dictionary.get("token") else APIHelper.SKIP
        # Return an object of this model
        return cls(number,
                   holder_name,
                   exp_month,
                   exp_year,
                   cvv,
                   billing_address,
                   brand,
                   billing_address_id,
                   metadata,
                   mtype,
                   options,
                   holder_document,
                   private_label,
                   label,
                   id,
                   token)
