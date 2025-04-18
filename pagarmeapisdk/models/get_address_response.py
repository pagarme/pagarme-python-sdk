# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetAddressResponse(object):

    """Implementation of the 'GetAddressResponse' model.

    Response object for getting an Address

    Attributes:
        id (str): The model property of type str.
        street (str): The model property of type str.
        number (str): The model property of type str.
        complement (str): The model property of type str.
        zip_code (str): The model property of type str.
        neighborhood (str): The model property of type str.
        city (str): The model property of type str.
        state (str): The model property of type str.
        country (str): The model property of type str.
        status (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        customer (GetCustomerResponse): The model property of type
            GetCustomerResponse.
        metadata (Dict[str, str]): The model property of type Dict[str, str].
        line_1 (str): Line 1 for address
        line_2 (str): Line 2 for address
        deleted_at (datetime): The model property of type datetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "street": 'street',
        "number": 'number',
        "complement": 'complement',
        "zip_code": 'zip_code',
        "neighborhood": 'neighborhood',
        "city": 'city',
        "state": 'state',
        "country": 'country',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "customer": 'customer',
        "metadata": 'metadata',
        "line_1": 'line_1',
        "line_2": 'line_2',
        "deleted_at": 'deleted_at'
    }

    _optionals = [
        'id',
        'street',
        'number',
        'complement',
        'zip_code',
        'neighborhood',
        'city',
        'state',
        'country',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'metadata',
        'line_1',
        'line_2',
        'deleted_at',
    ]

    _nullables = [
        'id',
        'street',
        'number',
        'complement',
        'zip_code',
        'neighborhood',
        'city',
        'state',
        'country',
        'status',
        'created_at',
        'updated_at',
        'customer',
        'metadata',
        'line_1',
        'line_2',
        'deleted_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 street=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 complement=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 neighborhood=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 line_1=APIHelper.SKIP,
                 line_2=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP):
        """Constructor for the GetAddressResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if street is not APIHelper.SKIP:
            self.street = street 
        if number is not APIHelper.SKIP:
            self.number = number 
        if complement is not APIHelper.SKIP:
            self.complement = complement 
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code 
        if neighborhood is not APIHelper.SKIP:
            self.neighborhood = neighborhood 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if country is not APIHelper.SKIP:
            self.country = country 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if line_1 is not APIHelper.SKIP:
            self.line_1 = line_1 
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 

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
        from pagarmeapisdk.models.get_customer_response import GetCustomerResponse

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        street = dictionary.get("street") if "street" in dictionary.keys() else APIHelper.SKIP
        number = dictionary.get("number") if "number" in dictionary.keys() else APIHelper.SKIP
        complement = dictionary.get("complement") if "complement" in dictionary.keys() else APIHelper.SKIP
        zip_code = dictionary.get("zip_code") if "zip_code" in dictionary.keys() else APIHelper.SKIP
        neighborhood = dictionary.get("neighborhood") if "neighborhood" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("city") if "city" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("state") if "state" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get("country") if "country" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'customer' in dictionary.keys():
            customer = GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        else:
            customer = APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        line_1 = dictionary.get("line_1") if "line_1" in dictionary.keys() else APIHelper.SKIP
        line_2 = dictionary.get("line_2") if "line_2" in dictionary.keys() else APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   street,
                   number,
                   complement,
                   zip_code,
                   neighborhood,
                   city,
                   state,
                   country,
                   status,
                   created_at,
                   updated_at,
                   customer,
                   metadata,
                   line_1,
                   line_2,
                   deleted_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'street={(self.street if hasattr(self, "street") else None)!r}, '
                f'number={(self.number if hasattr(self, "number") else None)!r}, '
                f'complement={(self.complement if hasattr(self, "complement") else None)!r}, '
                f'zip_code={(self.zip_code if hasattr(self, "zip_code") else None)!r}, '
                f'neighborhood={(self.neighborhood if hasattr(self, "neighborhood") else None)!r}, '
                f'city={(self.city if hasattr(self, "city") else None)!r}, '
                f'state={(self.state if hasattr(self, "state") else None)!r}, '
                f'country={(self.country if hasattr(self, "country") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!r}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!r}, '
                f'line_1={(self.line_1 if hasattr(self, "line_1") else None)!r}, '
                f'line_2={(self.line_2 if hasattr(self, "line_2") else None)!r}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'street={(self.street if hasattr(self, "street") else None)!s}, '
                f'number={(self.number if hasattr(self, "number") else None)!s}, '
                f'complement={(self.complement if hasattr(self, "complement") else None)!s}, '
                f'zip_code={(self.zip_code if hasattr(self, "zip_code") else None)!s}, '
                f'neighborhood={(self.neighborhood if hasattr(self, "neighborhood") else None)!s}, '
                f'city={(self.city if hasattr(self, "city") else None)!s}, '
                f'state={(self.state if hasattr(self, "state") else None)!s}, '
                f'country={(self.country if hasattr(self, "country") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'customer={(self.customer if hasattr(self, "customer") else None)!s}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!s}, '
                f'line_1={(self.line_1 if hasattr(self, "line_1") else None)!s}, '
                f'line_2={(self.line_2 if hasattr(self, "line_2") else None)!s}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!s})')
