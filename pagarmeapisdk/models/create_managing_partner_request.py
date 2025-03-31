# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_register_information_address_request import CreateRegisterInformationAddressRequest
from pagarmeapisdk.models.create_register_information_phone_request import CreateRegisterInformationPhoneRequest


class CreateManagingPartnerRequest(object):

    """Implementation of the 'CreateManagingPartnerRequest' model.

    Managing Partner Request

    Attributes:
        name (str): The model property of type str.
        email (str): The model property of type str.
        document (str): The model property of type str.
        mother_name (str): The model property of type str.
        birthdate (str): The model property of type str.
        monthly_income (int): The model property of type int.
        professional_occupation (str): The model property of type str.
        self_declared_legal_representative (bool): The model property of type
            bool.
        address (CreateRegisterInformationAddressRequest): The model property
            of type CreateRegisterInformationAddressRequest.
        phone_numbers (List[CreateRegisterInformationPhoneRequest]): The model
            property of type List[CreateRegisterInformationPhoneRequest].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email": 'email',
        "document": 'document',
        "birthdate": 'birthdate',
        "monthly_income": 'monthly_income',
        "professional_occupation": 'professional_occupation',
        "self_declared_legal_representative": 'self_declared_legal_representative',
        "address": 'address',
        "phone_numbers": 'phone_numbers',
        "mother_name": 'mother_name'
    }

    _optionals = [
        'mother_name',
    ]

    _nullables = [
        'mother_name',
    ]

    def __init__(self,
                 name=None,
                 email=None,
                 document=None,
                 birthdate=None,
                 monthly_income=None,
                 professional_occupation=None,
                 self_declared_legal_representative=None,
                 address=None,
                 phone_numbers=None,
                 mother_name=APIHelper.SKIP):
        """Constructor for the CreateManagingPartnerRequest class"""

        # Initialize members of the class
        self.name = name 
        self.email = email 
        self.document = document 
        if mother_name is not APIHelper.SKIP:
            self.mother_name = mother_name 
        self.birthdate = birthdate 
        self.monthly_income = monthly_income 
        self.professional_occupation = professional_occupation 
        self.self_declared_legal_representative = self_declared_legal_representative 
        self.address = address 
        self.phone_numbers = phone_numbers 

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
        birthdate = dictionary.get("birthdate") if dictionary.get("birthdate") else None
        monthly_income = dictionary.get("monthly_income") if dictionary.get("monthly_income") else None
        professional_occupation = dictionary.get("professional_occupation") if dictionary.get("professional_occupation") else None
        self_declared_legal_representative = dictionary.get("self_declared_legal_representative") if "self_declared_legal_representative" in dictionary.keys() else None
        address = CreateRegisterInformationAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        phone_numbers = None
        if dictionary.get('phone_numbers') is not None:
            phone_numbers = [CreateRegisterInformationPhoneRequest.from_dictionary(x) for x in dictionary.get('phone_numbers')]
        mother_name = dictionary.get("mother_name") if "mother_name" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email,
                   document,
                   birthdate,
                   monthly_income,
                   professional_occupation,
                   self_declared_legal_representative,
                   address,
                   phone_numbers,
                   mother_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'email={self.email!r}, '
                f'document={self.document!r}, '
                f'mother_name={(self.mother_name if hasattr(self, "mother_name") else None)!r}, '
                f'birthdate={self.birthdate!r}, '
                f'monthly_income={self.monthly_income!r}, '
                f'professional_occupation={self.professional_occupation!r}, '
                f'self_declared_legal_representative={self.self_declared_legal_representative!r}, '
                f'address={self.address!r}, '
                f'phone_numbers={self.phone_numbers!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'email={self.email!s}, '
                f'document={self.document!s}, '
                f'mother_name={(self.mother_name if hasattr(self, "mother_name") else None)!s}, '
                f'birthdate={self.birthdate!s}, '
                f'monthly_income={self.monthly_income!s}, '
                f'professional_occupation={self.professional_occupation!s}, '
                f'self_declared_legal_representative={self.self_declared_legal_representative!s}, '
                f'address={self.address!s}, '
                f'phone_numbers={self.phone_numbers!s})')
