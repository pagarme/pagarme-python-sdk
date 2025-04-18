# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_phone_number_response import GetPhoneNumberResponse
from pagarmeapisdk.models.get_register_information_address_response import GetRegisterInformationAddressResponse


class GetManagingPartnerResponse(object):

    """Implementation of the 'GetManagingPartnerResponse' model.

    Response object for getting an ManagingPartnerResponse

    Attributes:
        name (str): The model property of type str.
        email (str): The model property of type str.
        document (str): The model property of type str.
        mtype (str): The model property of type str.
        mother_name (str): The model property of type str.
        birthdate (str): The model property of type str.
        monthly_income (str): The model property of type str.
        professional_occupation (str): The model property of type str.
        self_declared_representative (bool): The model property of type bool.
        address (GetRegisterInformationAddressResponse): The model property of
            type GetRegisterInformationAddressResponse.
        phone_numbers (List[GetPhoneNumberResponse]): The model property of
            type List[GetPhoneNumberResponse].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "email": 'email',
        "document": 'document',
        "mtype": 'type',
        "mother_name": 'mother_name',
        "birthdate": 'birthdate',
        "monthly_income": 'monthly_income',
        "professional_occupation": 'professional_occupation',
        "self_declared_representative": 'self_declared_representative',
        "address": 'address',
        "phone_numbers": 'phone_numbers'
    }

    _optionals = [
        'name',
        'email',
        'document',
        'mtype',
        'mother_name',
        'birthdate',
        'monthly_income',
        'professional_occupation',
        'self_declared_representative',
        'address',
        'phone_numbers',
    ]

    _nullables = [
        'name',
        'email',
        'document',
        'mtype',
        'mother_name',
        'birthdate',
        'monthly_income',
        'professional_occupation',
        'address',
        'phone_numbers',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 document=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 mother_name=APIHelper.SKIP,
                 birthdate=APIHelper.SKIP,
                 monthly_income=APIHelper.SKIP,
                 professional_occupation=APIHelper.SKIP,
                 self_declared_representative=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 phone_numbers=APIHelper.SKIP):
        """Constructor for the GetManagingPartnerResponse class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if email is not APIHelper.SKIP:
            self.email = email 
        if document is not APIHelper.SKIP:
            self.document = document 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if mother_name is not APIHelper.SKIP:
            self.mother_name = mother_name 
        if birthdate is not APIHelper.SKIP:
            self.birthdate = birthdate 
        if monthly_income is not APIHelper.SKIP:
            self.monthly_income = monthly_income 
        if professional_occupation is not APIHelper.SKIP:
            self.professional_occupation = professional_occupation 
        if self_declared_representative is not APIHelper.SKIP:
            self.self_declared_representative = self_declared_representative 
        if address is not APIHelper.SKIP:
            self.address = address 
        if phone_numbers is not APIHelper.SKIP:
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
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        email = dictionary.get("email") if "email" in dictionary.keys() else APIHelper.SKIP
        document = dictionary.get("document") if "document" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        mother_name = dictionary.get("mother_name") if "mother_name" in dictionary.keys() else APIHelper.SKIP
        birthdate = dictionary.get("birthdate") if "birthdate" in dictionary.keys() else APIHelper.SKIP
        monthly_income = dictionary.get("monthly_income") if "monthly_income" in dictionary.keys() else APIHelper.SKIP
        professional_occupation = dictionary.get("professional_occupation") if "professional_occupation" in dictionary.keys() else APIHelper.SKIP
        self_declared_representative = dictionary.get("self_declared_representative") if "self_declared_representative" in dictionary.keys() else APIHelper.SKIP
        if 'address' in dictionary.keys():
            address = GetRegisterInformationAddressResponse.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        else:
            address = APIHelper.SKIP
        if 'phone_numbers' in dictionary.keys():
            phone_numbers = [GetPhoneNumberResponse.from_dictionary(x) for x in dictionary.get('phone_numbers')] if dictionary.get('phone_numbers') else None
        else:
            phone_numbers = APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   email,
                   document,
                   mtype,
                   mother_name,
                   birthdate,
                   monthly_income,
                   professional_occupation,
                   self_declared_representative,
                   address,
                   phone_numbers)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'email={(self.email if hasattr(self, "email") else None)!r}, '
                f'document={(self.document if hasattr(self, "document") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'mother_name={(self.mother_name if hasattr(self, "mother_name") else None)!r}, '
                f'birthdate={(self.birthdate if hasattr(self, "birthdate") else None)!r}, '
                f'monthly_income={(self.monthly_income if hasattr(self, "monthly_income") else None)!r}, '
                f'professional_occupation={(self.professional_occupation if hasattr(self, "professional_occupation") else None)!r}, '
                f'self_declared_representative={(self.self_declared_representative if hasattr(self, "self_declared_representative") else None)!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r}, '
                f'phone_numbers={(self.phone_numbers if hasattr(self, "phone_numbers") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'email={(self.email if hasattr(self, "email") else None)!s}, '
                f'document={(self.document if hasattr(self, "document") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'mother_name={(self.mother_name if hasattr(self, "mother_name") else None)!s}, '
                f'birthdate={(self.birthdate if hasattr(self, "birthdate") else None)!s}, '
                f'monthly_income={(self.monthly_income if hasattr(self, "monthly_income") else None)!s}, '
                f'professional_occupation={(self.professional_occupation if hasattr(self, "professional_occupation") else None)!s}, '
                f'self_declared_representative={(self.self_declared_representative if hasattr(self, "self_declared_representative") else None)!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s}, '
                f'phone_numbers={(self.phone_numbers if hasattr(self, "phone_numbers") else None)!s})')
