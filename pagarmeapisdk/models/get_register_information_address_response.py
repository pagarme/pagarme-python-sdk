# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetRegisterInformationAddressResponse(object):

    """Implementation of the 'GetRegisterInformationAddressResponse' model.

    Response object for getting an RegisterInformationAddress

    Attributes:
        street (str): TODO: type description here.
        complementary (str): TODO: type description here.
        street_number (str): TODO: type description here.
        neighborhood (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        zip_code (str): TODO: type description here.
        reference_point (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "street": 'street',
        "complementary": 'complementary',
        "street_number": 'street_number',
        "neighborhood": 'neighborhood',
        "city": 'city',
        "state": 'state',
        "zip_code": 'zip_code',
        "reference_point": 'reference_point'
    }

    _optionals = [
        'street',
        'complementary',
        'street_number',
        'neighborhood',
        'city',
        'state',
        'zip_code',
        'reference_point',
    ]

    _nullables = [
        'street',
        'complementary',
        'street_number',
        'neighborhood',
        'city',
        'state',
        'zip_code',
        'reference_point',
    ]

    def __init__(self,
                 street=APIHelper.SKIP,
                 complementary=APIHelper.SKIP,
                 street_number=APIHelper.SKIP,
                 neighborhood=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 reference_point=APIHelper.SKIP):
        """Constructor for the GetRegisterInformationAddressResponse class"""

        # Initialize members of the class
        if street is not APIHelper.SKIP:
            self.street = street 
        if complementary is not APIHelper.SKIP:
            self.complementary = complementary 
        if street_number is not APIHelper.SKIP:
            self.street_number = street_number 
        if neighborhood is not APIHelper.SKIP:
            self.neighborhood = neighborhood 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code 
        if reference_point is not APIHelper.SKIP:
            self.reference_point = reference_point 

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
        street = dictionary.get("street") if "street" in dictionary.keys() else APIHelper.SKIP
        complementary = dictionary.get("complementary") if "complementary" in dictionary.keys() else APIHelper.SKIP
        street_number = dictionary.get("street_number") if "street_number" in dictionary.keys() else APIHelper.SKIP
        neighborhood = dictionary.get("neighborhood") if "neighborhood" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("state") if "state" in dictionary.keys() else APIHelper.SKIP
        zip_code = dictionary.get("zip_code") if "zip_code" in dictionary.keys() else APIHelper.SKIP
        reference_point = dictionary.get("reference_point") if "reference_point" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(street,
                   complementary,
                   street_number,
                   neighborhood,
                   city,
                   state,
                   zip_code,
                   reference_point)