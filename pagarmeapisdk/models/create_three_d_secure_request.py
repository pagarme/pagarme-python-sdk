# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class CreateThreeDSecureRequest(object):

    """Implementation of the 'CreateThreeDSecureRequest' model.

    Creates a 3D-S authentication payment

    Attributes:
        mpi (string): The MPI Vendor (MerchantPlugin)
        cavv (string): The Cardholder Authentication Verification value
        eci (string): The Electronic Commerce Indicator value
        transaction_id (string): The TransactionId value (XID)
        success_url (string): The success URL after the authentication
        ds_transaction_id (string): Directory Service Transaction Identifier
        version (string): ThreeDSecure Version

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mpi": 'mpi',
        "cavv": 'cavv',
        "eci": 'eci',
        "transaction_id": 'transaction_id',
        "success_url": 'success_url',
        "ds_transaction_id": 'ds_transaction_id',
        "version": 'version'
    }

    _optionals = [
        'cavv',
        'eci',
        'transaction_id',
        'success_url',
        'ds_transaction_id',
        'version',
    ]

    def __init__(self,
                 mpi=None,
                 cavv=APIHelper.SKIP,
                 eci=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 success_url=APIHelper.SKIP,
                 ds_transaction_id=APIHelper.SKIP,
                 version=APIHelper.SKIP):
        """Constructor for the CreateThreeDSecureRequest class"""

        # Initialize members of the class
        self.mpi = mpi 
        if cavv is not APIHelper.SKIP:
            self.cavv = cavv 
        if eci is not APIHelper.SKIP:
            self.eci = eci 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if success_url is not APIHelper.SKIP:
            self.success_url = success_url 
        if ds_transaction_id is not APIHelper.SKIP:
            self.ds_transaction_id = ds_transaction_id 
        if version is not APIHelper.SKIP:
            self.version = version 

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

        mpi = dictionary.get("mpi") if dictionary.get("mpi") else None
        cavv = dictionary.get("cavv") if dictionary.get("cavv") else APIHelper.SKIP
        eci = dictionary.get("eci") if dictionary.get("eci") else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        success_url = dictionary.get("success_url") if dictionary.get("success_url") else APIHelper.SKIP
        ds_transaction_id = dictionary.get("ds_transaction_id") if dictionary.get("ds_transaction_id") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        # Return an object of this model
        return cls(mpi,
                   cavv,
                   eci,
                   transaction_id,
                   success_url,
                   ds_transaction_id,
                   version)
