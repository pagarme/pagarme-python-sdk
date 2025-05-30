# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetPixBankAccountResponse(object):

    """Implementation of the 'GetPixBankAccountResponse' model.

    Payer's bank details.

    Attributes:
        bank_name (str): The model property of type str.
        ispb (str): The model property of type str.
        branch_code (str): The model property of type str.
        account_number (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_name": 'bank_name',
        "ispb": 'ispb',
        "branch_code": 'branch_code',
        "account_number": 'account_number'
    }

    _optionals = [
        'bank_name',
        'ispb',
        'branch_code',
        'account_number',
    ]

    _nullables = [
        'bank_name',
        'ispb',
        'branch_code',
        'account_number',
    ]

    def __init__(self,
                 bank_name=APIHelper.SKIP,
                 ispb=APIHelper.SKIP,
                 branch_code=APIHelper.SKIP,
                 account_number=APIHelper.SKIP):
        """Constructor for the GetPixBankAccountResponse class"""

        # Initialize members of the class
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name 
        if ispb is not APIHelper.SKIP:
            self.ispb = ispb 
        if branch_code is not APIHelper.SKIP:
            self.branch_code = branch_code 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 

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
        bank_name = dictionary.get("bank_name") if "bank_name" in dictionary.keys() else APIHelper.SKIP
        ispb = dictionary.get("ispb") if "ispb" in dictionary.keys() else APIHelper.SKIP
        branch_code = dictionary.get("branch_code") if "branch_code" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("account_number") if "account_number" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(bank_name,
                   ispb,
                   branch_code,
                   account_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'bank_name={(self.bank_name if hasattr(self, "bank_name") else None)!r}, '
                f'ispb={(self.ispb if hasattr(self, "ispb") else None)!r}, '
                f'branch_code={(self.branch_code if hasattr(self, "branch_code") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'bank_name={(self.bank_name if hasattr(self, "bank_name") else None)!s}, '
                f'ispb={(self.ispb if hasattr(self, "ispb") else None)!s}, '
                f'branch_code={(self.branch_code if hasattr(self, "branch_code") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s})')
