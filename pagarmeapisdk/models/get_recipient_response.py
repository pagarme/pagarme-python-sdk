# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_automatic_anticipation_response import GetAutomaticAnticipationResponse
from pagarmeapisdk.models.get_bank_account_response import *
from pagarmeapisdk.models.get_gateway_recipient_response import GetGatewayRecipientResponse
from pagarmeapisdk.models.get_transfer_settings_response import GetTransferSettingsResponse


class GetRecipientResponse(object):

    """Implementation of the 'GetRecipientResponse' model.

    Recipient response

    Attributes:
        id (string): Id
        name (string): Name
        email (string): Email
        document (string): Document
        description (string): Description
        mtype (string): Type
        status (string): Status
        created_at (datetime): Creation date
        updated_at (datetime): Last update date
        deleted_at (datetime): Deletion date
        default_bank_account (GetBankAccountResponse): Default bank account
        gateway_recipients (list of GetGatewayRecipientResponse): Info about
            the recipient on the gateway
        metadata (dict): Metadata
        automatic_anticipation_settings (GetAutomaticAnticipationResponse):
            TODO: type description here.
        transfer_settings (GetTransferSettingsResponse): TODO: type
            description here.
        code (string): Recipient code
        payment_mode (string): Payment mode

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "email": 'email',
        "document": 'document',
        "description": 'description',
        "mtype": 'type',
        "status": 'status',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "deleted_at": 'deleted_at',
        "default_bank_account": 'default_bank_account',
        "gateway_recipients": 'gateway_recipients',
        "metadata": 'metadata',
        "code": 'code',
        "payment_mode": 'payment_mode',
        "automatic_anticipation_settings": 'automatic_anticipation_settings',
        "transfer_settings": 'transfer_settings'
    }

    _optionals = [
        'automatic_anticipation_settings',
        'transfer_settings',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 email=None,
                 document=None,
                 description=None,
                 mtype=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 deleted_at=None,
                 default_bank_account=None,
                 gateway_recipients=None,
                 metadata=None,
                 code=None,
                 payment_mode='bank_transfer',
                 automatic_anticipation_settings=APIHelper.SKIP,
                 transfer_settings=APIHelper.SKIP):
        """Constructor for the GetRecipientResponse class"""

        # Initialize members of the class
        self.id = id 
        self.name = name 
        self.email = email 
        self.document = document 
        self.description = description 
        self.mtype = mtype 
        self.status = status 
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None 
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None 
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None 
        self.default_bank_account = default_bank_account 
        self.gateway_recipients = gateway_recipients 
        self.metadata = metadata 
        if automatic_anticipation_settings is not APIHelper.SKIP:
            self.automatic_anticipation_settings = automatic_anticipation_settings 
        if transfer_settings is not APIHelper.SKIP:
            self.transfer_settings = transfer_settings 
        self.code = code 
        self.payment_mode = payment_mode 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        email = dictionary.get("email") if dictionary.get("email") else None
        document = dictionary.get("document") if dictionary.get("document") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        default_bank_account = GetBankAccountResponse.from_dictionary(dictionary.get('default_bank_account')) if dictionary.get('default_bank_account') else None
        gateway_recipients = None
        if dictionary.get('gateway_recipients') is not None:
            gateway_recipients = [GetGatewayRecipientResponse.from_dictionary(x) for x in dictionary.get('gateway_recipients')]
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        code = dictionary.get("code") if dictionary.get("code") else None
        payment_mode = dictionary.get("payment_mode") if dictionary.get("payment_mode") else 'bank_transfer'
        automatic_anticipation_settings = GetAutomaticAnticipationResponse.from_dictionary(dictionary.get('automatic_anticipation_settings')) if 'automatic_anticipation_settings' in dictionary.keys() else APIHelper.SKIP 
        transfer_settings = GetTransferSettingsResponse.from_dictionary(dictionary.get('transfer_settings')) if 'transfer_settings' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(id,
                   name,
                   email,
                   document,
                   description,
                   mtype,
                   status,
                   created_at,
                   updated_at,
                   deleted_at,
                   default_bank_account,
                   gateway_recipients,
                   metadata,
                   code,
                   payment_mode,
                   automatic_anticipation_settings,
                   transfer_settings)
