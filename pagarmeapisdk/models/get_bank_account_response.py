# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetBankAccountResponse(object):

    """Implementation of the 'GetBankAccountResponse' model.

    Attributes:
        id (str): Id
        holder_name (str): Holder name
        holder_type (str): Holder type
        bank (str): Bank
        branch_number (str): Branch number
        branch_check_digit (str): Branch check digit
        account_number (str): Account number
        account_check_digit (str): Account check digit
        mtype (str): Bank account type
        status (str): Bank account status
        created_at (datetime): Creation date
        updated_at (datetime): Last update date
        deleted_at (datetime): Deletion date
        recipient (GetRecipientResponse): Recipient
        metadata (Dict[str, str]): Metadata
        pix_key (str): Pix Key

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "holder_name": 'holder_name',
        "holder_type": 'holder_type',
        "bank": 'bank',
        "branch_number": 'branch_number',
        "branch_check_digit": 'branch_check_digit',
        "account_number": 'account_number',
        "account_check_digit": 'account_check_digit',
        "mtype": 'type',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "deleted_at": 'deleted_at',
        "recipient": 'recipient',
        "metadata": 'metadata',
        "pix_key": 'pix_key'
    }

    _optionals = [
        'id',
        'holder_name',
        'holder_type',
        'bank',
        'branch_number',
        'branch_check_digit',
        'account_number',
        'account_check_digit',
        'mtype',
        'status',
        'created_at',
        'updated_at',
        'deleted_at',
        'recipient',
        'metadata',
        'pix_key',
    ]

    _nullables = [
        'id',
        'holder_name',
        'holder_type',
        'bank',
        'branch_number',
        'branch_check_digit',
        'account_number',
        'account_check_digit',
        'mtype',
        'status',
        'created_at',
        'updated_at',
        'deleted_at',
        'recipient',
        'metadata',
        'pix_key',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 holder_name=APIHelper.SKIP,
                 holder_type=APIHelper.SKIP,
                 bank=APIHelper.SKIP,
                 branch_number=APIHelper.SKIP,
                 branch_check_digit=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_check_digit=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 deleted_at=APIHelper.SKIP,
                 recipient=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 pix_key=APIHelper.SKIP):
        """Constructor for the GetBankAccountResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if holder_name is not APIHelper.SKIP:
            self.holder_name = holder_name 
        if holder_type is not APIHelper.SKIP:
            self.holder_type = holder_type 
        if bank is not APIHelper.SKIP:
            self.bank = bank 
        if branch_number is not APIHelper.SKIP:
            self.branch_number = branch_number 
        if branch_check_digit is not APIHelper.SKIP:
            self.branch_check_digit = branch_check_digit 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_check_digit is not APIHelper.SKIP:
            self.account_check_digit = account_check_digit 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if status is not APIHelper.SKIP:
            self.status = status 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if deleted_at is not APIHelper.SKIP:
            self.deleted_at = APIHelper.apply_datetime_converter(deleted_at, APIHelper.RFC3339DateTime) if deleted_at else None 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if pix_key is not APIHelper.SKIP:
            self.pix_key = pix_key 

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
        from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        holder_name = dictionary.get("holder_name") if "holder_name" in dictionary.keys() else APIHelper.SKIP
        holder_type = dictionary.get("holder_type") if "holder_type" in dictionary.keys() else APIHelper.SKIP
        bank = dictionary.get("bank") if "bank" in dictionary.keys() else APIHelper.SKIP
        branch_number = dictionary.get("branch_number") if "branch_number" in dictionary.keys() else APIHelper.SKIP
        branch_check_digit = dictionary.get("branch_check_digit") if "branch_check_digit" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("account_number") if "account_number" in dictionary.keys() else APIHelper.SKIP
        account_check_digit = dictionary.get("account_check_digit") if "account_check_digit" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'deleted_at' in dictionary.keys():
            deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        else:
            deleted_at = APIHelper.SKIP
        if 'recipient' in dictionary.keys():
            recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None
        else:
            recipient = APIHelper.SKIP
        metadata = dictionary.get("metadata") if "metadata" in dictionary.keys() else APIHelper.SKIP
        pix_key = dictionary.get("pix_key") if "pix_key" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   holder_name,
                   holder_type,
                   bank,
                   branch_number,
                   branch_check_digit,
                   account_number,
                   account_check_digit,
                   mtype,
                   status,
                   created_at,
                   updated_at,
                   deleted_at,
                   recipient,
                   metadata,
                   pix_key)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'holder_name={(self.holder_name if hasattr(self, "holder_name") else None)!r}, '
                f'holder_type={(self.holder_type if hasattr(self, "holder_type") else None)!r}, '
                f'bank={(self.bank if hasattr(self, "bank") else None)!r}, '
                f'branch_number={(self.branch_number if hasattr(self, "branch_number") else None)!r}, '
                f'branch_check_digit={(self.branch_check_digit if hasattr(self, "branch_check_digit") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_check_digit={(self.account_check_digit if hasattr(self, "account_check_digit") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!r}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!r}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!r}, '
                f'pix_key={(self.pix_key if hasattr(self, "pix_key") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'holder_name={(self.holder_name if hasattr(self, "holder_name") else None)!s}, '
                f'holder_type={(self.holder_type if hasattr(self, "holder_type") else None)!s}, '
                f'bank={(self.bank if hasattr(self, "bank") else None)!s}, '
                f'branch_number={(self.branch_number if hasattr(self, "branch_number") else None)!s}, '
                f'branch_check_digit={(self.branch_check_digit if hasattr(self, "branch_check_digit") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_check_digit={(self.account_check_digit if hasattr(self, "account_check_digit") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'deleted_at={(self.deleted_at if hasattr(self, "deleted_at") else None)!s}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!s}, '
                f'metadata={(self.metadata if hasattr(self, "metadata") else None)!s}, '
                f'pix_key={(self.pix_key if hasattr(self, "pix_key") else None)!s})')
