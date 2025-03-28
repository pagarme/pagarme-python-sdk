# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest


class CreateCustomerRequest(object):

    """Implementation of the 'CreateCustomerRequest' model.

    Request for creating a new customer

    Attributes:
        name (str): Name
        email (str): Email
        document (str): Document number. Only numbers, no special characters.
        mtype (str): Person type. Can be either 'individual' or 'company'
        address (CreateAddressRequest): The customer's address
        metadata (Dict[str, str]): Metadata
        phones (CreatePhonesRequest): The model property of type
            CreatePhonesRequest.
        code (str): Customer code
        gender (str): Customer Gender
        document_type (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email": 'email',
        "document": 'document',
        "mtype": 'type',
        "address": 'address',
        "metadata": 'metadata',
        "phones": 'phones',
        "code": 'code',
        "gender": 'gender',
        "document_type": 'document_type'
    }

    _optionals = [
        'gender',
        'document_type',
    ]

    def __init__(self,
                 name=None,
                 email=None,
                 document=None,
                 mtype=None,
                 address=None,
                 metadata=None,
                 phones=None,
                 code=None,
                 gender=APIHelper.SKIP,
                 document_type=APIHelper.SKIP):
        """Constructor for the CreateCustomerRequest class"""

        # Initialize members of the class
        self.name = name 
        self.email = email 
        self.document = document 
        self.mtype = mtype 
        self.address = address 
        self.metadata = metadata 
        self.phones = phones 
        self.code = code 
        if gender is not APIHelper.SKIP:
            self.gender = gender 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 

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
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        address = CreateAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        phones = CreatePhonesRequest.from_dictionary(dictionary.get('phones')) if dictionary.get('phones') else None
        code = dictionary.get("code") if dictionary.get("code") else None
        gender = dictionary.get("gender") if dictionary.get("gender") else APIHelper.SKIP
        document_type = dictionary.get("document_type") if dictionary.get("document_type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email,
                   document,
                   mtype,
                   address,
                   metadata,
                   phones,
                   code,
                   gender,
                   document_type)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'email={self.email!r}, '
                f'document={self.document!r}, '
                f'mtype={self.mtype!r}, '
                f'address={self.address!r}, '
                f'metadata={self.metadata!r}, '
                f'phones={self.phones!r}, '
                f'code={self.code!r}, '
                f'gender={(self.gender if hasattr(self, "gender") else None)!r}, '
                f'document_type={(self.document_type if hasattr(self, "document_type") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'email={self.email!s}, '
                f'document={self.document!s}, '
                f'mtype={self.mtype!s}, '
                f'address={self.address!s}, '
                f'metadata={self.metadata!s}, '
                f'phones={self.phones!s}, '
                f'code={self.code!s}, '
                f'gender={(self.gender if hasattr(self, "gender") else None)!s}, '
                f'document_type={(self.document_type if hasattr(self, "document_type") else None)!s})')
