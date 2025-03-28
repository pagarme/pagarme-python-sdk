# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetRetryTransactionInformationResponse(object):

    """Implementation of the 'GetRetryTransactionInformationResponse' model.

    Response object for getting an RetryTransactionInformation

    Attributes:
        brand_failure_return_code (str): The model property of type str.
        transaction_limit (int): The model property of type int.
        transaction_date_limit (datetime): The model property of type datetime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand_failure_return_code": 'brand_failure_return_code',
        "transaction_limit": 'transaction_limit',
        "transaction_date_limit": 'transaction_date_limit'
    }

    _nullables = [
        'brand_failure_return_code',
        'transaction_limit',
        'transaction_date_limit',
    ]

    def __init__(self,
                 brand_failure_return_code=None,
                 transaction_limit=None,
                 transaction_date_limit=None):
        """Constructor for the GetRetryTransactionInformationResponse class"""

        # Initialize members of the class
        self.brand_failure_return_code = brand_failure_return_code 
        self.transaction_limit = transaction_limit 
        self.transaction_date_limit = APIHelper.apply_datetime_converter(transaction_date_limit, APIHelper.RFC3339DateTime) if transaction_date_limit else None 

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
        brand_failure_return_code = dictionary.get("brand_failure_return_code") if dictionary.get("brand_failure_return_code") else None
        transaction_limit = dictionary.get("transaction_limit") if dictionary.get("transaction_limit") else None
        transaction_date_limit = APIHelper.RFC3339DateTime.from_value(dictionary.get("transaction_date_limit")).datetime if dictionary.get("transaction_date_limit") else None
        # Return an object of this model
        return cls(brand_failure_return_code,
                   transaction_limit,
                   transaction_date_limit)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'brand_failure_return_code={self.brand_failure_return_code!r}, '
                f'transaction_limit={self.transaction_limit!r}, '
                f'transaction_date_limit={self.transaction_date_limit!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'brand_failure_return_code={self.brand_failure_return_code!s}, '
                f'transaction_limit={self.transaction_limit!s}, '
                f'transaction_date_limit={self.transaction_date_limit!s})')
